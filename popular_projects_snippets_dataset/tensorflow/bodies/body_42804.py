# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function with valid argspec."""

def func(m, n, l, k=4):
    exit(2 * m + l + n * k)

partial_func = functools.partial(func, n=7, l=2)
argspec = tf_inspect.ArgSpec(
    args=['m', 'n', 'l', 'k'],
    varargs=None,
    keywords=None,
    defaults=(7, 2, 4))

self.assertEqual(argspec, tf_inspect.getargspec(partial_func))
