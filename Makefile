# NOTE: This is based on Qeeseburger's Makefile.
.PHONY: test stylecheck style

test:
	python3 -B -m pytest neoconverter/tests --cov neoconverter

stylecheck:
	flake8 neoconverter/ setup.py
	black --check -l 79 neoconverter/ setup.py

style:
	black -l 79 neoconverter/ setup.py
