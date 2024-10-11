# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(positional, func=1, func_and_positional=2, kwargs=3):
    exit((positional, func, func_and_positional, kwargs))

kwargs = {}
self.assertEqual(
    tf_inspect.getcallargs(func, 0, **kwargs), {
        'positional': 0,
        'func': 1,
        'func_and_positional': 2,
        'kwargs': 3
    })
kwargs = dict(func=4, func_and_positional=5, kwargs=6)
self.assertEqual(
    tf_inspect.getcallargs(func, 0, **kwargs), {
        'positional': 0,
        'func': 4,
        'func_and_positional': 5,
        'kwargs': 6
    })
