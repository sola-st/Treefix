# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
api_info = self.makeApiInfoFromParamSpecs("ConvertAttributes", ["x"], {},
                                          {"x": attr_type})
tensor_converter = self.makeTensorConverter()

params = [attr_val]
inferred = Convert(api_info, tensor_converter, params)
self.assertEqual(inferred.types, [])
self.assertEqual(inferred.type_lists, [])
self.assertEqual(inferred.lengths, [])
self.assertLen(params, 1)
actual = params[0]
self.assertEqual(actual, expected)

# Check that we got the actual types we expected.  (Note that in Python,
# two values may be equal even if they have different types.)
self.assertIs(type(actual), type(expected))
if isinstance(expected, list):
    self.assertLen(actual, len(expected))
    for (actual_item, expected_item) in zip(actual, expected):
        self.assertIs(type(actual_item), type(expected_item))
