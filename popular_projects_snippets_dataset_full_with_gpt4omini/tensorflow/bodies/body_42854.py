# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertTrue(tf_inspect.ismethod(TestDecoratedClass().two))
self.assertFalse(tf_inspect.ismethod(test_decorated_function))
