# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
api_info = self.makeApiInfoFromParamSpecs("Foo", ["x"], {},
                                          {"x": attr_type})
tensor_converter = self.makeTensorConverter()
with self.assertRaisesRegex(TypeError, message):
    Convert(api_info, tensor_converter, [attr_val])
