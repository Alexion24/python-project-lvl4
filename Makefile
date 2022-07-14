
install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

version:
		poetry run django-admin version

startproject:
		poetry run django-admin startproject task_manager .

runserver:
		poetry run python manage.py runserver

gunicorn:
		export DJANGO_SETTINGS_MODULE=task_manager.settings
		poetry run gunicorn task_manager.wsgi

requirements:
		poetry export --without-hashes -f requirements.txt -o requirements.txt

makemigrations:
		 poetry run python manage.py makemigrations

migrate:
		 poetry run python manage.py migrate

shell:
		poetry run python manage.py shell

#lint:
#	poetry run flake8 page_loader
#	poetry run flake8 tests
#
#test:
#	poetry run pytest -vv
#
#test-coverage:
#	poetry run pytest --cov=page_loader/ tests/ --cov-report xml
#
#selfcheck:
#	poetry check
#
#check: selfcheck test lint
#
#build: check
#	poetry build
#
#.PHONY: install test lint selfcheck check build




