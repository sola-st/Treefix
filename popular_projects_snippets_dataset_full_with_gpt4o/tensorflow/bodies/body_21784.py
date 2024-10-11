# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Validate `keep_input` argument to conditional batching functions."""
keep_input = ops.convert_to_tensor(keep_input)
if keep_input.shape.ndims is None:
    raise ValueError(
        "`keep_input` dimensions must be known at graph construction.")
if not enqueue_many and keep_input.shape.ndims == 1:
    raise ValueError(
        "`keep_input` cannot be a vector when `enqueue_many=False`.")
if keep_input.shape.ndims > 1:
    raise ValueError("`keep_input` must be 0 or 1 dimensions.")
exit(keep_input)
