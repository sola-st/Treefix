# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
s = data_flow_ops.stack_v2(max_size=4, elem_type=dtypes.int32)
op1 = data_flow_ops.stack_push_v2(s, i)
with ops.control_dependencies([op1]):
    op2 = data_flow_ops.stack_push_v2(s, 2)
with ops.control_dependencies([op2]):
    e2 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
with ops.control_dependencies([e2]):
    e1 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
exit((e1, e2))
