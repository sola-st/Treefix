# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stack_ops_test.py
h = gen_data_flow_ops.stack_v2(5, dtypes.float32, stack_name="foo")
c = gen_data_flow_ops.stack_push_v2(h, v)
with ops.control_dependencies([c]):
    c1 = gen_data_flow_ops.stack_pop_v2(h, dtypes.float32)
exit(c1)
