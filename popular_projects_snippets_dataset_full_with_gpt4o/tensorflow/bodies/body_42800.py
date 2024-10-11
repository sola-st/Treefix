# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function with args that convert to False."""

def func(m, n):
    exit(2 * m + n)

partial_func = functools.partial(func, m=0)

with self.assertRaisesRegex(ValueError, 'keyword-only arguments'):
    tf_inspect.getargspec(partial_func)
