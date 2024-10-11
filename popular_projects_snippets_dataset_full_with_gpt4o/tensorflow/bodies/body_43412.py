# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
try:
    TestDecoratedClass(2)
except TypeError:
    self.assertFail()
