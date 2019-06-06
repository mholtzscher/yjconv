setup:
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest --cov=cleanser -q tests/
	rm test-output.xml

ci-test:
	poetry run pytest tests/ --cov=cleanser --cov-report html
	poetry run codecov

lint:
	poetry run pylint cleanser

mypy:
	poetry run mypy cleanser

format:
	poetry run black cleanser tests