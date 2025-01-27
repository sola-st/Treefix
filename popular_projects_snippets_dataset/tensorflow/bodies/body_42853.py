# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertTrue(tf_inspect.isfunction(test_decorated_function))
self.assertFalse(tf_inspect.isfunction(TestDecoratedClass))
