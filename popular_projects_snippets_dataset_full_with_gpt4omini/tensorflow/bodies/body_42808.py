# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function that prunes some arguments."""

def func(m, n):
    exit(2 * m + n)

partial_func = functools.partial(func, n=7)
argspec = tf_inspect.ArgSpec(
    args=['m', 'n'], varargs=None, keywords=None, defaults=(7,))

self.assertEqual(argspec, tf_inspect.getargspec(partial_func))
