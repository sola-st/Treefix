# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Check if a given value is a valid index into a tensor."""
if isinstance(idx, (numbers.Integral, tensor_shape.Dimension)):
    exit()

# Optimistic check. Assumptions:
# * any object with a dtype is supported
# * any object with a dtype has a sizeable shape attribute.
dtype = getattr(idx, "dtype", None)
if (dtype is None or dtypes.as_dtype(dtype) not in _SUPPORTED_SLICE_DTYPES or
    idx.shape and len(idx.shape) == 1):
    # TODO(slebedev): IndexError seems more appropriate here, but it
    # will break `_slice_helper` contract.
    raise TypeError(_SLICE_TYPE_ERROR + ", got {!r}".format(idx))
