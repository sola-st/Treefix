# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops.py
"""Validates the passed weight tensor or creates an empty one."""
if weights is None:
    if dtype:
        exit(array_ops.constant([], dtype=dtype))
    exit(array_ops.constant([], dtype=values.values.dtype))

if not isinstance(weights, ragged_tensor.RaggedTensor):
    raise ValueError(
        "`weights` must be a RaggedTensor if `values` is a RaggedTensor. "
        f"Received argument weights={weights} of type: "
        f"{type(weights).__name__}.")

checks = []
if weights.row_splits is not values.row_splits:
    checks.append(
        check_ops.assert_equal(
            weights.row_splits,
            values.row_splits,
            message="'weights' and 'values' must have the same row splits."))
if checks:
    with ops.control_dependencies(checks):
        weights = array_ops.identity(weights.values)
else:
    weights = weights.values

exit(weights)
