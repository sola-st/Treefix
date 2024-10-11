# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
if isinstance(actual, ops.Tensor):
    self.assertAllEqual(actual, expected)
else:
    self.assertEqual(actual, expected)
self.assertIs(type(actual), type(expected))
