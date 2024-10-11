# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    h = gen_data_flow_ops.stack_v2(
        -1, elem_type=dtypes.float32, stack_name="foo")
    c = gen_data_flow_ops.stack_push_v2(h, [[4.0, 5.0]])
    with ops.control_dependencies([c]):
        c1 = gen_data_flow_ops.stack_pop_v2(h, dtypes.float32)
    self.assertAllClose([[4.0, 5.0]], self.evaluate(c1))
