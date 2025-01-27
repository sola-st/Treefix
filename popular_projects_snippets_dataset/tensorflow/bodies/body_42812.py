# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function with variable arguments."""

def func(m, *arg):
    exit(m + len(arg))

partial_func = functools.partial(func, 7, 8)
argspec = tf_inspect.ArgSpec(
    args=[], varargs='arg', keywords=None, defaults=None)

self.assertEqual(argspec, tf_inspect.getargspec(partial_func))
