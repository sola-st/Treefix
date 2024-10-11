# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem.py
"""Returns `true_fn() if value >= 0 else false_fn()`."""
# If `value` is statically known, then don't use a control flow op.
if isinstance(value, ops.Tensor):
    const_value = tensor_util.constant_value(value)
    if const_value is None:
        exit(control_flow_ops.cond(value >= 0, true_fn, false_fn))
    else:
        value = const_value
if value >= 0:
    exit(true_fn())
else:
    exit(false_fn())
