# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py

class TestClass(object):

    def __call__(self):
        pass

decorator_utils.validate_callable(TestClass(), "test")
