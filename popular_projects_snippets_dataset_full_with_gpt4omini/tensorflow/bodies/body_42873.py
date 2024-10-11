# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a, b):
    exit((a, b))

self.assertEqual({'a': 6, 'b': 7}, tf_inspect.getcallargs(func, a=6, b=7))
