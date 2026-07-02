# Architecture

Universal AI Knowledge Graph is built around a simple production pattern:

1. Connectors load source records.
2. Ingestion normalises each record into a document.
3. Chunking prepares text for retrieval.
4. Embedding providers create vector representations.
5. Entity and relationship extraction builds graph context.
6. Storage adapters persist documents, chunks, vectors, entities and relationships.
7. Retrieval combines semantic similarity with graph context and provenance.

## Source model

Every source becomes a `Document` with:

- `workspace_id`
- `source`
- `external_id`
- `title`
- `body`
- `metadata`

This keeps connector implementation simple and makes provenance consistent.

## Connector SDK

All connectors implement:

```python
class Connector:
    async def load(self) -> AsyncIterator[DocumentIn]: ...
```

This means enterprise integrations can stream records without loading entire systems into memory.

## Storage strategy

The current implementation includes an in-memory store so the project runs immediately. The intended production store is:

- Postgres for workspaces, documents, chunks, metadata and audit logs
- pgvector for embeddings
- Optional graph database adapter for deeper traversal workloads

The service boundary is intentionally adapter-based so these can be swapped without rewriting the API.

## Retrieval strategy

Search should combine:

- Query embedding similarity
- Metadata filters
- Keyword matching
- Entity matches
- Graph relationships
- Permissions and workspace boundaries

The first implementation exposes the shape of this workflow and is ready for durable index adapters.

## Security boundaries

- API-key protection is available for private deployments.
- Workspace IDs are first-class to support multi-tenancy.
- Source metadata is preserved for auditability.
- Connectors should never log secrets or raw credentials.
- Production deployments should add SSO/OIDC, RBAC and row-level security.
