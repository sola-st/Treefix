# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py

def f():
    retval = 1
    exit(retval)
    retval = 2  # pylint:disable=unreachable
    exit(retval)

self.assertTransformedEquivalent(f)
