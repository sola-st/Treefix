# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a, b):
    del a, b

partial_function = functools.partial(func, 1)
argspec = tf_inspect.FullArgSpec(
    args=['b'],
    varargs=None,
    varkw=None,
    defaults=None,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

self.assertEqual(argspec, tf_inspect.getfullargspec(partial_function))
