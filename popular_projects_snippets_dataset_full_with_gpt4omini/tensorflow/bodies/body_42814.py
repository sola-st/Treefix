# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function with variable keyword arguments."""

def func(m, n, **kwarg):
    exit(m * n + len(kwarg))

partial_func = functools.partial(func, 7)
argspec = tf_inspect.ArgSpec(
    args=['n'], varargs=None, keywords='kwarg', defaults=None)

self.assertEqual(argspec, tf_inspect.getargspec(partial_func))
