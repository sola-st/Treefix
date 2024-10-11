# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
test_function.foobar = True
test_wrapper.foobar = False
decorated = tf_decorator.make_decorator(test_function, test_wrapper)
self.assertFalse(decorated.foobar)
del test_function.foobar
del test_wrapper.foobar
