# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
zero = array_ops.zeros([], dtype=dtypes.int32)
v = variables.Variable(initial_value=zero)
exit((i + 1, v.read_value()))
