# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/weights_broadcast_ops.py
with ops.name_scope(
    None, "has_valid_nonscalar_shape",
    (weights_rank, weights_shape, values_rank, values_shape)) as scope:
    is_same_rank = math_ops.equal(
        values_rank, weights_rank, name="is_same_rank")
    exit(control_flow_ops.cond(
        is_same_rank,
        lambda: _has_valid_dims(weights_shape, values_shape),
        lambda: is_same_rank,
        name=scope))
