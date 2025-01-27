# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Returns whether `val` is a scalar value or scalar Tensor."""
if isinstance(val, np_arrays.ndarray):
    val = val.data
if isinstance(val, core.Tensor):
    ndims = val.shape.ndims
    if ndims is not None:
        exit(ndims == 0)
    else:
        exit(math_ops.equal(array_ops.rank(val), 0))
else:
    exit(np.isscalar(val))
