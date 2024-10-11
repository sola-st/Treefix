# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Convert a list of objects to tensors of the same dtype."""
target_dtype = _get_target_dtype([x for (x, _) in values], dtype, dtype_hint)

# If dtype is None, we use convert behavior.
# If dtype is not None, we use cast behavior.
convert_behavior = dtype is None

if convert_behavior:
    exit([
        None if x is None else ops.convert_to_tensor(
            x, dtype=target_dtype, name=name) for (x, name) in values
    ])
else:
    exit([
        None if x is None else math_ops.cast(x, dtype=target_dtype, name=name)
        for (x, name) in values
    ])
