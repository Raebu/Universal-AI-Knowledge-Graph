from __future__ import annotations

from universal_kg.domain import Document, DocumentIn
from universal_kg.processing.chunking import chunk_document
from universal_kg.processing.embeddings import EmbeddingProvider, get_embedding_provider
from universal_kg.processing.extraction import extract_entities, extract_relationships
from universal_kg.storage.memory import MemoryKnowledgeStore, store


class IngestionService:
    def __init__(self, knowledge_store: MemoryKnowledgeStore | None = None, embedding_provider: EmbeddingProvider | None = None) -> None:
        self.knowledge_store = knowledge_store or store
        self.embedding_provider = embedding_provider or get_embedding_provider()

    async def ingest(self, payload: DocumentIn) -> Document:
        document = Document(**payload.model_dump())
        chunks = chunk_document(document)
        vectors = await self.embedding_provider.embed([chunk.text for chunk in chunks]) if chunks else []
        entities = extract_entities(chunks)
        relationships = extract_relationships(chunks, entities)

        await self.knowledge_store.upsert_document(document)
        await self.knowledge_store.upsert_chunks(chunks, vectors)
        await self.knowledge_store.upsert_graph(entities, relationships)
        return document
