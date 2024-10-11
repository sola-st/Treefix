# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with ops.control_dependencies([x]):
    a = constant_op.constant(np.ones(2000), dtype=dtypes.float32)
    v = gen_data_flow_ops.stack_push(h, a, swap_memory=True)
with ops.control_dependencies([v]):
    exit(math_ops.add(x, 1))
