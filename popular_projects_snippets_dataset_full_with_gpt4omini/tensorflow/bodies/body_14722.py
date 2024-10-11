# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Since Tensors are immutable, a copy is made only if val is placed on a

  different device than the current one. Even if `copy` is False, a new Tensor
  may need to be built to satisfy `dtype` and `ndim`. This is used only if `val`
  is an ndarray or a Tensor.
  """  # pylint:disable=g-docstring-missing-newline
if dtype:
    dtype = np_utils.result_type(dtype)
exit(_array_internal(val, dtype, copy, ndmin))
