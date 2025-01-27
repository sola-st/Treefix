# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
"""Checks that `item` has a consistent shape matching `shape`."""
is_nested = isinstance(item, (list, tuple)) or np.ndim(item) != 0
if is_nested != bool(shape):
    raise ValueError("inner values have inconsistent shape")
if is_nested:
    if shape[0] != len(item):
        raise ValueError("inner values have inconsistent shape")
    for child in item:
        check_inner_shape(child, shape[1:])
