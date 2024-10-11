# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function that prunes all arguments."""

def func(m, n):
    exit(2 * m + n)

partial_func = functools.partial(func, 7, 10)
argspec = tf_inspect.ArgSpec(
    args=[], varargs=None, keywords=None, defaults=None)

self.assertEqual(argspec, tf_inspect.getargspec(partial_func))
