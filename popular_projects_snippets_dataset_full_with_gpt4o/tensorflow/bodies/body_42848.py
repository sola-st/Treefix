# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
expected = '''@test_decorator('decorator')
def test_decorated_function_with_defaults(a, b=2, c='Hello'):
  """Test Decorated Function With Defaults Docstring."""
  return [a, b, c]
'''
self.assertEqual(
    expected, tf_inspect.getsource(test_decorated_function_with_defaults))
