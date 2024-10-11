# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
e1 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
with ops.control_dependencies([e1]):
    e2 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
exit((e1, e2))
