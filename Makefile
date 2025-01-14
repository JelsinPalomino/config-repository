.PHONY: release test

artifacts: test
	python setup.py sdist bdist_wheel

prepforbuild:
	pip install --upgrade twine setuptools wheel

uploadtest:
	twine upload --repository testpypi dist/*

release:
	twine upload dist/* 

test-cov:
	pytest --cov-report html --cov=foo tests/

test:
	pytest -v -W ignore


