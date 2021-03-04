# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="wmq-pysample",
    version="0.1.0",
    description="WMQ client sample",
    license="MIT",
    author="Gábor Bereczki",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)
