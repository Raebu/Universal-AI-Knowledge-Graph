from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class SourceType(StrEnum):
    MANUAL = "manual"
    PDF = "pdf"
    EMAIL = "email"
    SLACK = "slack"
    CRM = "crm"
    GITHUB = "github"
    DATABASE = "database"
    JSON = "json"
    CSV = "csv"


class EntityType(StrEnum):
    PERSON = "person"
    ORGANISATION = "organisation"
    PRODUCT = "product"
    PROJECT = "project"
    SYSTEM = "system"
    CONCEPT = "concept"
    DOCUMENT = "document"
    ISSUE = "issue"
    DATABASE_TABLE = "database_table"


class DocumentIn(BaseModel):
    workspace_id: str = Field(min_length=1)
    source: SourceType | str
    external_id: str | None = None
    title: str
    body: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    workspace_id: str
    source: str
    external_id: str | None = None
    title: str
    body: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Chunk(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    document_id: str
    workspace_id: str
    text: str
    ordinal: int
    metadata: dict[str, Any] = Field(default_factory=dict)


class Entity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    workspace_id: str
    name: str
    type: EntityType | str = EntityType.CONCEPT
    metadata: dict[str, Any] = Field(default_factory=dict)


class Relationship(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    workspace_id: str
    subject: str
    predicate: str
    object: str
    evidence_chunk_id: str | None = None
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    metadata: dict[str, Any] = Field(default_factory=dict)


class SearchRequest(BaseModel):
    workspace_id: str
    query: str
    limit: int = Field(default=10, ge=1, le=50)
    include_graph: bool = True


class SearchHit(BaseModel):
    document_id: str
    chunk_id: str
    title: str
    text: str
    score: float
    source: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class SearchResponse(BaseModel):
    query: str
    hits: list[SearchHit]
    related_entities: list[Entity] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)
