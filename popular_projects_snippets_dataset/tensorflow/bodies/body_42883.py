# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a=1):
    exit(a)

self.assertEqual({'a': 3}, tf_inspect.getcallargs(func, a=3))
