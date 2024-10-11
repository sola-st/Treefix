# Extracted from https://stackoverflow.com/questions/15746675/how-to-write-a-python-module-package
.
└── hellostackoverflow/
    ├── __init__.py
    └── hellostackoverflow.py

.
├── setup.py
└── hellostackoverflow/
    ├── __init__.py
    └── hellostackoverflow.py

from setuptools import setup

setup(
    name='hellostackoverflow',
    version='0.0.1',
    description='a pip-installable package example',
    license='MIT',
    packages=['hellostackoverflow'],
    author='Benjamin Gerfelder',
    author_email='benjamin.gerfelder@gmail.com',
    keywords=['example'],
    url='https://github.com/bgse/hellostackoverflow'
)

.
├── LICENCE.txt
├── README.rst
├── setup.py
└── hellostackoverflow/
    ├── __init__.py
    └── hellostackoverflow.py

pip install setuptools

python setup.py sdist

.
├── dist/
├── hellostackoverflow.egg-info/
├── LICENCE.txt
├── README.rst
├── setup.py
└── hellostackoverflow/
    ├── __init__.py
    └── hellostackoverflow.py

pip install ./dist/hellostackoverflow-0.0.1.tar.gz

Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
from hellostackoverflow import hellostackoverflow
hellostackoverflow.greeting()
'Hello Stack Overflow!'

pip install twine

twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pip install --index-url https://test.pypi.org/simple/ hellostackoverflow

