# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu) as sess:
    h = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")
    c = gen_data_flow_ops.stack_push(h, [[4.0, 5.0]])
    with ops.control_dependencies([c]):
        c1 = gen_data_flow_ops.stack_close(h)
    self.evaluate(c1)
