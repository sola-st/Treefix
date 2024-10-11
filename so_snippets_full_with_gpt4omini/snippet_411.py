# Extracted from https://stackoverflow.com/questions/2051192/what-is-a-python-egg
# setup.py
from setuptools import setup, find_packages
setup(
    name = "mymath",
    version = "0.1",
    packages = find_packages()
    )

 $ python setup.py bdist_egg

