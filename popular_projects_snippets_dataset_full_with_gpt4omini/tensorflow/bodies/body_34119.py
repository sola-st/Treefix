# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    h1 = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")
    c1 = gen_data_flow_ops.stack_push(h1, 4.0)
    with ops.control_dependencies([c1]):
        c1 = gen_data_flow_ops.stack_pop(h1, dtypes.float32)
    h2 = gen_data_flow_ops._stack(dtypes.float32, stack_name="bar")
    c2 = gen_data_flow_ops.stack_push(h2, 5.0)
    with ops.control_dependencies([c2]):
        c2 = gen_data_flow_ops.stack_pop(h2, dtypes.float32)
    r = c1 + c2
    self.assertAllClose(9.0, self.evaluate(r))
