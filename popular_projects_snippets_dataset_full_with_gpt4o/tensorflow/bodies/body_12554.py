# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops.py
"""Validates the passed weight tensor or creates an empty one."""
if weights is None:
    if dtype:
        exit(array_ops.constant([], dtype=dtype))
    exit(array_ops.constant([], dtype=values.dtype))

if not isinstance(weights, ops.Tensor):
    raise ValueError(
        "Argument `weights` must be a tf.Tensor if `values` is a tf.Tensor. "
        f"Received weights={weights} of type: {type(weights).__name__}")

exit(weights)
