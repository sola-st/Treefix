# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function that doesn't have valid argspec."""

def func(m, n, l, k=4):
    exit(2 * m + l + n * k)

partial_func = functools.partial(func, n=7)

with self.assertRaisesRegex(ValueError, 'keyword-only arguments'):
    tf_inspect.getargspec(partial_func)
