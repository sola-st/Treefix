# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertEqual(
    inspect.getmembers(TestDecoratedClass),
    tf_inspect.getmembers(TestDecoratedClass))
