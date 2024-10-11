# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu) as sess:
    h = gen_data_flow_ops.stack_v2(
        -1, elem_type=dtypes.float32, stack_name="foo")
    c1 = gen_data_flow_ops.stack_close_v2(h)
    self.evaluate(c1)
