# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a=1, b=2):
    exit((a, b))

self.assertEqual({'a': 3, 'b': 2}, tf_inspect.getcallargs(func, a=3))
