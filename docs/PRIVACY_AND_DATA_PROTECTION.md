# Privacy and Data Protection

Universal AI Knowledge Graph is intended for enterprise knowledge retrieval, so privacy and data protection must be treated as core product features.

## Data categories

The platform may process:

- Documents and PDFs
- Emails and message exports
- CRM records
- GitHub issues, pull requests and code metadata
- Database rows and schema information
- User-generated search queries

## Recommended production controls

- Define a data processing agreement for hosted deployments.
- Configure source-specific retention periods.
- Redact secrets and unnecessary personal data during ingestion.
- Limit connector scopes to read-only unless write actions are explicitly required.
- Store tenant data with strict workspace isolation.
- Maintain audit logs for ingestion, search and administrative actions.
- Provide deletion workflows by source, workspace, user and document ID.
- Document subprocessors for hosted deployments.

## Default project stance

This repository does not sell data, does not train models by default, and does not require external AI providers for local development. The default embedding provider is deterministic and local. Production operators can opt into external model providers by setting environment variables.
