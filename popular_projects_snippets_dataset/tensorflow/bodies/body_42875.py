# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func(a=13):
    exit(a)

self.assertEqual({'a': 13}, tf_inspect.getcallargs(func))
