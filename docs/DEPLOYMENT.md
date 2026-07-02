# Production Deployment

## Recommended baseline

- Run the API behind a managed HTTPS load balancer.
- Set `UKG_ENVIRONMENT=production`.
- Set `UKG_API_KEY` or replace it with OIDC/JWT middleware.
- Use managed Postgres with pgvector for durable storage.
- Use a managed secret store for connector credentials.
- Enable centralised log collection.
- Restrict CORS to trusted application domains.
- Configure backup, retention and deletion policies.

## Docker deployment

```bash
cp .env.example .env
# edit .env with production values
docker compose up --build -d
curl http://localhost:8000/health
```

## Kubernetes notes

Create separate deployments for:

- API
- Ingestion workers
- Scheduled connector syncs

Use:

- Horizontal pod autoscaling for API reads
- Queue-backed workers for ingestion
- Network policies limiting database access
- Read-only service accounts for source connectors

## Required production TODOs

The current repository is a production-ready foundation, but these items remain before handling real enterprise customer data at scale:

- Replace in-memory store with Postgres/pgvector persistence.
- Add SSO/OIDC and workspace-level RBAC.
- Add encrypted connector credential storage.
- Add durable audit log tables.
- Add full deletion/export workflows for data protection requests.
