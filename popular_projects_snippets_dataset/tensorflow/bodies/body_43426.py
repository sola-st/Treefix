# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
test_function.foobar = True
decorated = tf_decorator.make_decorator(test_function, test_wrapper)
self.assertTrue(decorated.foobar)
del test_function.foobar
