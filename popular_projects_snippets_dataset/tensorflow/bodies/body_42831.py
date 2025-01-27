# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getfullargspec on partial function that prunes all arguments."""

def func(m, n):
    exit(2 * m + n)

partial_func = functools.partial(func, 7, 10)
argspec = tf_inspect.FullArgSpec(
    args=[],
    varargs=None,
    varkw=None,
    defaults=None,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))
