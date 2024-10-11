# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getfullargspec on partial function with variable arguments."""

def func(m, *arg):
    exit(m + len(arg))

partial_func = functools.partial(func, 7, 8)
argspec = tf_inspect.FullArgSpec(
    args=[],
    varargs='arg',
    varkw=None,
    defaults=None,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))
