# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def empty():
    pass

self.assertEqual({}, tf_inspect.getcallargs(empty))
