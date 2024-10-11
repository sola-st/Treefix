# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
_, target = tf_decorator.unwrap(test_function)
self.assertIs(test_function, target)
