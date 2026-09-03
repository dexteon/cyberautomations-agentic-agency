APP=cyberautomations-agentic-agency

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f app

lint:
	python -m py_compile src/cyberautomations_agency/*.py src/cyberautomations_agency/tools/*.py src/cyberautomations_agency/workflows/*.py

run:
	PYTHONPATH=src python -m cyberautomations_agency.main

test-config:
	PYTHONPATH=src python -m cyberautomations_agency.main --dry-run
