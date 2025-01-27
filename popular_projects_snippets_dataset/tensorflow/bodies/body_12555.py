# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops.py
"""Validates the passed weight tensor or creates an empty one."""
if weights is None:
    if dtype:
        exit(array_ops.constant([], dtype=dtype))
    exit(array_ops.constant([], dtype=values.values.dtype))

if not isinstance(weights, sparse_tensor.SparseTensor):
    raise ValueError(
        "Argument `weights` must be a SparseTensor if `values` is a "
        f"SparseTensor. Received weights={weights} of type: "
        f"{type(weights).__name__}")

checks = []
if weights.dense_shape is not values.dense_shape:
    checks.append(
        check_ops.assert_equal(
            weights.dense_shape,
            values.dense_shape,
            message="'weights' and 'values' must have the same dense shape."))
if weights.indices is not values.indices:
    checks.append(
        check_ops.assert_equal(
            weights.indices,
            values.indices,
            message="'weights' and 'values' must have the same indices.")
    )
if checks:
    with ops.control_dependencies(checks):
        weights = array_ops.identity(weights.values)
else:
    weights = weights.values

exit(weights)
