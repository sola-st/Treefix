# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function with only positional arguments."""

def func(m, n):
    exit(2 * m + n)

partial_func = functools.partial(func, 7)
argspec = tf_inspect.ArgSpec(
    args=['n'], varargs=None, keywords=None, defaults=None)

self.assertEqual(argspec, tf_inspect.getargspec(partial_func))
