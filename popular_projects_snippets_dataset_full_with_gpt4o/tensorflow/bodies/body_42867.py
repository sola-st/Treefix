# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a):
    exit(a)

self.assertEqual({'a': 5}, tf_inspect.getcallargs(func, 5))
