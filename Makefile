SHELL := /bin/bash

PROJECT := test-travis
LOCALPATH := $(CURDIR)
PYTHONPATH := $(LOCALPATH)
PYTHON_BIN := $(VIRTUAL_ENV)/bin

.PHONY: check run publish

run:
	python $(PYTHONPATH)/foo.py

check:
	python $(PYTHONPATH)/foo_test.py -v

publish:
	git pull origin master
	git add $(PYTHONPATH)/foo_test.py
	git add $(PYTHONPATH)/foo.py
	git commit -m "auto-regenerate from make"
	git push origin master
