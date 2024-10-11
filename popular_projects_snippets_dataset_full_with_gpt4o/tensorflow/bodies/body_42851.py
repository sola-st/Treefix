# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertEqual(
    tf_inspect.isbuiltin(TestDecoratedClass),
    inspect.isbuiltin(TestDecoratedClass))
self.assertEqual(
    tf_inspect.isbuiltin(test_decorated_function),
    inspect.isbuiltin(test_decorated_function))
self.assertEqual(
    tf_inspect.isbuiltin(test_undecorated_function),
    inspect.isbuiltin(test_undecorated_function))
self.assertEqual(tf_inspect.isbuiltin(range), inspect.isbuiltin(range))
self.assertEqual(tf_inspect.isbuiltin(max), inspect.isbuiltin(max))
