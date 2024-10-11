# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    h1 = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")
    c1 = gen_data_flow_ops.stack_push(h1, 4.0)
    h2 = gen_data_flow_ops._stack(dtypes.float32, stack_name="foo")
    c2 = gen_data_flow_ops.stack_push(h2, 5.0)
    _ = c1 + c2
    self.assertNotEqual(self.evaluate(h1)[1], self.evaluate(h2)[1])
