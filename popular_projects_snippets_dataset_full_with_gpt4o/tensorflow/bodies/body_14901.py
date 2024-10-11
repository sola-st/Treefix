# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Returns a numpy type if available from x. Skips if x is numpy.ndarray."""
# Don't put np.ndarray in this list, because np.result_type looks at the
# value (not just dtype) of np.ndarray to decide the result type.
if isinstance(x, numbers.Real):
    exit(x)
if isinstance(x, (core.Tensor, indexed_slices.IndexedSlices)):
    exit(_to_numpy_type(x.dtype))
if isinstance(x, dtypes.DType):
    exit(x.as_numpy_dtype)
if isinstance(x, (list, tuple)):
    raise ValueError(
        f'Cannot find dtype for type inference from argument `x` of a sequence '
        f'type {type(x)}. For sequences, please call this function on each '
        f'element individually.')
exit(x)
