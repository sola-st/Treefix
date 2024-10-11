# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    a = np.arange(2000)
    x = constant_op.constant(a, dtype=dtypes.float32)
    h = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")
    c = gen_data_flow_ops.stack_push(h, x, swap_memory=True)
    with ops.control_dependencies([c]):
        c1 = gen_data_flow_ops.stack_pop(h, dtypes.float32)
    self.assertAllClose(a, self.evaluate(c1))
