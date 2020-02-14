#!/usr/bin/env python
# NOTE: This file is derived from Qeeseburger's setup.py file.

from setuptools import find_packages, setup

classes = """
    Development Status :: 3 - Alpha
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3 :: Only
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split("\n") if s]

description = "Simple parser for NEO CSV-for-Excel files"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="neoconverter",
    version="0.0.0",
    license="BSD",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="neoconverter development team",
    author_email="mfedarko@ucsd.edu",
    maintainer="neoconverter development team",
    maintainer_email="mfedarko@ucsd.edu",
    url="https://github.com/fedarko/neo-csv-for-excel-parser",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "pandas"],
    # Based on how Altair splits up its requirements:
    # https://github.com/altair-viz/altair/blob/master/setup.py
    extras_require={
        "dev": ["pytest >= 4.2", "pytest-cov >= 2.0", "flake8", "black"]
    },
    classifiers=classifiers,
    entry_points={
        "console_scripts": ["convert-neo-excel=neoconverter.convert:convert"]
    },
    zip_safe=False,
    python_requires=">=3.5",
)
