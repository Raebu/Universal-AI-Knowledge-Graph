# Roadmap

## Phase 1: Production foundation

- FastAPI service with semantic search endpoints
- Connector SDK
- Local deterministic embeddings for development
- Optional OpenAI embedding provider
- PDF and JSON connectors
- In-memory store for simple deployments and tests
- Docker Compose stack
- CI with lint, type checks, tests and image build

## Phase 2: Durable enterprise storage

- Postgres persistence for documents, chunks and metadata
- pgvector vector index
- Alembic migrations
- Tenant and workspace administration
- Audit logs
- Data retention controls

## Phase 3: Enterprise connectors

- Gmail / Google Workspace
- Slack
- GitHub repositories, issues and pull requests
- Salesforce and HubSpot CRM
- SharePoint and Google Drive
- SQL database crawler
- Web crawler with allow-list and robots controls

## Phase 4: Knowledge graph intelligence

- LLM-assisted entity resolution
- Configurable ontology
- Relationship confidence scoring
- Graph traversal search
- Explainable citations and source provenance
- Conflict and duplication detection

## Phase 5: AI application layer

- Chat over enterprise knowledge
- Answer generation with citations
- Permissions-aware retrieval
- Admin console
- Usage analytics
- Model and embedding provider marketplace
