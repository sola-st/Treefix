# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
"""Returns a PythonAPIParameterConverter for the given gen_op."""
api_info = _pywrap_python_api_info.PythonAPIInfo(op_name)
api_info.InitializeFromRegisteredOp(op_name)
exit(api_info)
