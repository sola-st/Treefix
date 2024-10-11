# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
expected = inspect.getsourcelines(
    test_decorated_function_with_defaults.decorated_target)
self.assertEqual(
    expected,
    tf_inspect.getsourcelines(test_decorated_function_with_defaults))
