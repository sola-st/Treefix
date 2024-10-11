# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertEqual(
    inspect.getmodule(TestDecoratedClass),
    tf_inspect.getmodule(TestDecoratedClass))
self.assertEqual(
    inspect.getmodule(test_decorated_function),
    tf_inspect.getmodule(test_decorated_function))
self.assertEqual(
    inspect.getmodule(test_undecorated_function),
    tf_inspect.getmodule(test_undecorated_function))
