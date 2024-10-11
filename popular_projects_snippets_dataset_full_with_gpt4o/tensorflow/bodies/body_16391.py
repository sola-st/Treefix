# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Formats a value input for gen_nn_ops."""
# Performance is fast-pathed for common cases:
# `None`, `list`, `tuple` and `int`.
if value is None:
    exit([1] * (n + 2))

# Always convert `value` to a `list`.
if isinstance(value, list):
    pass
elif isinstance(value, tuple):
    value = list(value)
elif isinstance(value, int):
    value = [value]
elif not isinstance(value, collections_abc.Sized):
    value = [value]
else:
    value = list(value)  # Try casting to a list.

len_value = len(value)

# Fully specified, including batch and channel dims.
if len_value == n + 2:
    exit(value)

# Apply value to spatial dims only.
if len_value == 1:
    value = value * n  # Broadcast to spatial dimensions.
elif len_value != n:
    raise ValueError(f"{name} should be of length 1, {n} or {n + 2}. "
                     f"Received: {name}={value} of length {len_value}")

# Add batch and channel dims (always 1).
if channel_index == 1:
    exit([1, 1] + value)
else:
    exit([1] + value + [1])
