# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
var = variables.VariableV1(1.0, name="variable_node")
self.assertIsNone(tensor_util.constant_value(var))
