# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
decorated = tf_decorator.make_decorator(test_function, test_wrapper)
wrapped_attr = getattr(decorated, '__wrapped__')
self.assertIs(test_function, wrapped_attr)
