# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stack_ops_test.py
h1 = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")
h2 = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")

c1 = gen_data_flow_ops.stack_push_v2(h1, v1)
with ops.control_dependencies([c1]):
    c2 = gen_data_flow_ops.stack_push_v2(h2, v2)
with ops.control_dependencies([c2]):
    pop1 = gen_data_flow_ops.stack_pop_v2(h1, dtypes.float32)
    pop2 = gen_data_flow_ops.stack_pop_v2(h2, dtypes.float32)
exit([pop1, pop2])
