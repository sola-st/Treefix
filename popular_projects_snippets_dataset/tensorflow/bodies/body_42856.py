# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertTrue(tf_inspect.isroutine(len))
self.assertFalse(tf_inspect.isroutine(TestDecoratedClass))
