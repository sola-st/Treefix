# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_info_test.py
api_info = self.makeConverterFromParamSpecs(api_name, param_names,
                                            input_specs, attr_specs)
self.assertEqual(api_info.DebugInfo().strip(), debug_info.strip())
