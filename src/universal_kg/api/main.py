from __future__ import annotations

import time
from collections.abc import Awaitable, Callable

from fastapi import Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from universal_kg.config import Settings, get_settings
from universal_kg.domain import Document, DocumentIn, SearchRequest, SearchResponse
from universal_kg.services.ingestion import IngestionService
from universal_kg.services.search import SearchService

app = FastAPI(
    title="Universal AI Knowledge Graph",
    version="0.1.0",
    default_response_class=ORJSONResponse,
    description="Enterprise semantic knowledge graph and AI-search API.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def require_api_key(x_api_key: str | None = Header(default=None), settings: Settings = Depends(get_settings)) -> None:
    if settings.api_key and x_api_key != settings.api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable[[Request], Awaitable[ORJSONResponse]]):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(round(time.perf_counter() - start, 6))
    return response


@app.get("/health")
async def health(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name, "environment": settings.environment}


@app.get("/metrics")
async def metrics() -> dict[str, int]:
    return {"process_up": 1}


@app.post("/v1/ingest", response_model=Document, dependencies=[Depends(require_api_key)])
async def ingest(payload: DocumentIn) -> Document:
    return await IngestionService().ingest(payload)


@app.post("/v1/search", response_model=SearchResponse, dependencies=[Depends(require_api_key)])
async def search(payload: SearchRequest) -> SearchResponse:
    return await SearchService().search(payload)
