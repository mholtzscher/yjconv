setup:
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest --cov=yjconv -q tests/
	rm test-output.xml

ci-test:
	poetry run pytest tests/ --cov=yjconv --cov-report html
	poetry run codecov

lint:
	poetry run pylint yjconv

mypy:
	poetry run mypy yjconv

format:
	poetry run black yjconv tests