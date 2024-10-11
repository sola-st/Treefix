# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Returns a numpy type if available from x. Skips if x is numpy.ndarray."""
# Don't put np.ndarray in this list, because np.result_type looks at the
# value (not just dtype) of np.ndarray to decide the result type.
if isinstance(x, numbers.Real):
    exit(x)
if isinstance(x, ops.Tensor):
    exit(x.dtype.as_numpy_dtype)
if isinstance(x, dtypes.DType):
    exit(x.as_numpy_dtype)
if isinstance(x, tensor_shape.TensorShape):
    exit(np.int32)
if isinstance(x, (list, tuple)):
    raise ValueError(f"Cannot determine dtype.  Got sequence {x}.")
exit(x)
