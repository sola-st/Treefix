# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
nx = math_ops.subtract(x, 1)
ny = y + gen_data_flow_ops.stack_pop(h, dtypes.float32)
exit([nx, ny])
