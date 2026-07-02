# Contributing

Thank you for contributing to Universal AI Knowledge Graph.

## Development setup

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
pytest
```

## Contribution areas

High-value contribution areas:

- New connectors
- Durable storage adapters
- Entity resolution
- Graph traversal retrieval
- Admin UI
- Security hardening
- Documentation and examples

## Connector checklist

Every connector should include:

- Clear name and source system
- Minimal permission scopes
- Pagination handling
- Rate limit behaviour
- Provenance metadata
- Tests with sample payloads
- Documentation for required environment variables

## Pull request standards

Before opening a pull request:

```bash
ruff check .
mypy src
pytest
```

Include tests for new behaviour and update docs when public APIs change.
