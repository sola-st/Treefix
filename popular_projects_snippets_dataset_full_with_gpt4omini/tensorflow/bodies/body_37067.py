# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
ni = math_ops.subtract(i, 1)
nx = x + gen_data_flow_ops.stack_pop_v2(s, dtypes.int32)
exit([ni, nx])
