# Security Policy

## Supported versions

The `main` branch is the actively supported development line.

## Reporting a vulnerability

Please do not open a public issue for security vulnerabilities.

Email the maintainers with:

- A clear description of the issue
- Reproduction steps
- Impact assessment
- Affected version or commit
- Suggested fix if available

## Security design principles

- Do not commit secrets.
- Use environment variables or a managed secret store.
- Keep connectors least-privilege.
- Log operational metadata, not raw sensitive content.
- Preserve source provenance for auditability.
- Encrypt data at rest in production infrastructure.
- Use TLS for all deployed API traffic.
- Add SSO/OIDC and RBAC before exposing the service to multiple organisations.

## Connector safety

Connectors may process sensitive enterprise data. New connectors must document:

- Required scopes and permissions
- Data read and write behaviour
- Rate limits
- Retention implications
- How credentials are stored and rotated
