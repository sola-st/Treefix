# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
api_info = self.makeApiInfoFromParamSpecs("TestFunc", param_names,
                                          input_specs, attr_specs)
tensor_converter = self.makeTensorConverter()
param_values = inputs()
with self.assertRaisesRegex(exception, message):
    Convert(api_info, tensor_converter, param_values)
