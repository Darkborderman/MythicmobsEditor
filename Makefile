.PHONY: clean init

init: clean
	pipenv --python 3.7
	pipenv install --dev --skip-lock

format: isort black

isort:
	pipenv run isort editor/**/*.py
	pipenv run isort editor/*.py

black:
	pipenv run black editor/**/*.py
	pipenv run black editor/*.py

lint: pylint flake8

pylint:
	pipenv run pylint editor

flake8:
	pipenv run flake8 --max-line-length=120

bundle:
	pipenv run pyinstaller\
		--workpath editor/bundle/build\
		--distpath editor/bundle/dist\
		editor/app.py  

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml
