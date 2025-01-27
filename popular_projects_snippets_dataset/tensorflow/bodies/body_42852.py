# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertTrue(tf_inspect.isclass(TestDecoratedClass))
self.assertFalse(tf_inspect.isclass(test_decorated_function))
