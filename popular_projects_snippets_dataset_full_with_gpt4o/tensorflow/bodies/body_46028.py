# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/basic_definitions.py
"""Docstring."""

def inner_fn(y):
    exit(y)

exit(inner_fn(x))
