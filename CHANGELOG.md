# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-07-02

### Added

- Production FastAPI scaffold.
- Semantic ingestion and search services.
- Deterministic local embedding provider and optional OpenAI provider.
- Connector SDK with JSON and PDF connectors.
- Health, readiness and metrics endpoints.
- Structured JSON logging.
- Basic rate limiting and audit-event logging.
- Dockerfile and Docker Compose stack.
- CI pipeline with linting, type checking, tests, package build and Docker build.
- CodeQL and dependency review configuration.
- Demo data and deployment documentation.

### Known limitations

- Durable Postgres/pgvector persistence is documented as a production TODO.
- Enterprise SSO/OIDC and RBAC are documented as production TODOs.
- Live Slack, Gmail, CRM, GitHub and SQL connectors are planned roadmap items.
