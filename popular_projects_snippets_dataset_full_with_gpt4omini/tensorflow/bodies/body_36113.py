# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
zero = array_ops.zeros([], dtype=dtypes.int32)
v = resource_variable_ops.ResourceVariable(initial_value=zero)
exit((i + 1, v.read_value()))
