# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
exit(control_flow_ops.cond(
    can_broadcast_from_b, true_fn=broadcast_from_b, false_fn=broadcast_noop))
