# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/weights_broadcast_ops.py
with ops.name_scope(
    None, "has_invalid_dims", (weights_shape, values_shape)) as scope:
    values_shape_2d = array_ops.expand_dims(values_shape, -1)
    valid_dims = array_ops.concat(
        (values_shape_2d, array_ops.ones_like(values_shape_2d)), axis=1)
    weights_shape_2d = array_ops.expand_dims(weights_shape, -1)
    invalid_dims = sets.set_difference(weights_shape_2d, valid_dims)
    num_invalid_dims = array_ops.size(
        invalid_dims.values, name="num_invalid_dims")
    exit(math_ops.equal(0, num_invalid_dims, name=scope))
