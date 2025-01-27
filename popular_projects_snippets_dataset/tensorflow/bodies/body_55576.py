# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_util_test.py
result = _op_def_util.ConvertPyObjectToAttributeType(value, attr_type)

# Check that we get the expected value(s).
self.assertEqual(expected, result)

# Check that we get the expected type(s).
self.assertEqual(type(expected), type(result))
if isinstance(result, list):
    for expected_item, result_item in zip(expected, result):
        self.assertEqual(type(expected_item), type(result_item))
