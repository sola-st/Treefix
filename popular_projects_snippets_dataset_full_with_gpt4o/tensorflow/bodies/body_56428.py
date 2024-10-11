# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_info_test.py
"""Returns a PythonAPIInfo built from the given specs."""
api_info = _pywrap_python_api_info.PythonAPIInfo(api_name)
api_info.InitializeFromParamSpecs(input_specs, attr_specs, param_names,
                                  defaults)
exit(api_info)
