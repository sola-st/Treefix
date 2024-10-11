# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
s = data_flow_ops.stack_v2(max_size=4, elem_type=dtypes.int32)

def loop_fn(_):
    exit(data_flow_ops.stack_push_v2(s, 7))

with self.assertRaisesRegex(ValueError, "StackPushV2 not allowed.*"):
    pfor_control_flow_ops.pfor(loop_fn, iters=2)
