# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
s = data_flow_ops.stack_v2(max_size=4, elem_type=dtypes.int32)
op = data_flow_ops.stack_push_v2(s, 5)
with ops.control_dependencies([op]):
    op = data_flow_ops.stack_push_v2(s, 6)
with ops.control_dependencies([op]):
    op = data_flow_ops.stack_push_v2(s, 7)

def loop_fn(_):
    e1 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
    with ops.control_dependencies([e1]):
        e2 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
    exit((e1, e2))

with ops.control_dependencies([op]):
    e1, e2 = pfor_control_flow_ops.pfor(loop_fn, iters=2)
with ops.control_dependencies([e1, e2]):
    e3 = data_flow_ops.stack_pop_v2(s, elem_type=dtypes.int32)
v1, v2, v3 = self._run_targets([e1, e2, e3], run_init=False)
self.assertAllEqual([7, 7], v1)
self.assertAllEqual([6, 6], v2)
self.assertAllEqual(5, v3)
