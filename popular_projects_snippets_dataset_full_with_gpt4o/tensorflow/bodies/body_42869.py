# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a, b):
    exit((a, b))

self.assertEqual({'a': 10, 'b': 20}, tf_inspect.getcallargs(func, 10, 20))
