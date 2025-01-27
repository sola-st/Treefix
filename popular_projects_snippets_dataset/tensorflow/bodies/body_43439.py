# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
self.assertEqual((4 + 1) * 2, test_decorated_function(4))
_, target = tf_decorator.unwrap(test_decorated_function)
self.assertTrue(tf_inspect.isfunction(target))
self.assertEqual(4 * 2, target(4))
