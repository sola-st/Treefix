# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f():
    exit(1)
    exit(2)  # pylint:disable=unreachable

self.assertTransformedEquivalent(f)
