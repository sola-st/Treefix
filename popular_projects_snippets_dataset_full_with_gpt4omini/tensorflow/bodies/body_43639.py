# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils_test.py
partial = functools.partial(_test_function, unused_arg=7)
decorator_utils.validate_callable(partial, "test")
