.PHONY: install lint format typecheck test build docker-build run

install:
	python -m pip install --upgrade pip
	pip install -e '.[dev]'

lint:
	ruff check .

format:
	ruff format .
	ruff check . --fix

typecheck:
	mypy src

test:
	pytest

build:
	python -m pip install build==1.2.2.post1
	python -m build

docker-build:
	docker build -t universal-ai-knowledge-graph:local .

run:
	uvicorn universal_kg.api.main:app --reload
