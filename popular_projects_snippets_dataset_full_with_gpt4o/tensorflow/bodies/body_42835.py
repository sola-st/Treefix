# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getfullargspec.

    Tests on partial function with variable keyword arguments.
    """

def func(m, n, **kwarg):
    exit(m * n + len(kwarg))

partial_func = functools.partial(func, 7)
argspec = tf_inspect.FullArgSpec(
    args=['n'],
    varargs=None,
    varkw='kwarg',
    defaults=None,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))
