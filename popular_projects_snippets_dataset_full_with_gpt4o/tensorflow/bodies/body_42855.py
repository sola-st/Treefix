# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertTrue(
    tf_inspect.ismodule(inspect.getmodule(inspect.currentframe())))
self.assertFalse(tf_inspect.ismodule(test_decorated_function))
