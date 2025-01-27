# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stack_ops_test.py
"""Different stacks with the same name do not interfere."""
with self.cached_session(use_gpu=use_gpu) as sess:
    h1 = gen_data_flow_ops.stack_v2(
        -1, elem_type=dtypes.float32, stack_name="foo")
    h2 = gen_data_flow_ops.stack_v2(
        -1, elem_type=dtypes.float32, stack_name="foo")

    c1 = gen_data_flow_ops.stack_push_v2(h1, 4.0)
    with ops.control_dependencies([c1]):
        c2 = gen_data_flow_ops.stack_push_v2(h2, 5.0)
    with ops.control_dependencies([c2]):
        pop1 = gen_data_flow_ops.stack_pop_v2(h1, dtypes.float32)
        pop2 = gen_data_flow_ops.stack_pop_v2(h2, dtypes.float32)

    out1, out2 = self.evaluate([pop1, pop2])
    self.assertAllClose(out1, 4.0)
    self.assertAllClose(out2, 5.0)
