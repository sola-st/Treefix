# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a=0):
    exit(a)

self.assertEqual({'a': 1}, tf_inspect.getcallargs(func, 1))
