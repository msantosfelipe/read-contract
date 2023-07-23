.PHONY: run-local run-flask db-up db-down freeze create-venv activate-venv deactivate-venv

run-local:
	python3 src/flask_service.py --local

run-flask:
	python3 src/flask_service.py

db-up:
	cd docker && docker-compose up -d

db-down:
	docker stop mongodb

# Python env
freeze:
	pip freeze > requirements.txt

create-venv:
	python3 -m venv read-contract

activate-venv:
	source ./read-contract/bin/activate

deactivate-venv:
	deactivate
