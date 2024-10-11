# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Converts shape to a format understood by list_ops for element_shape.

  If `shape` is already a `Tensor` it is returned as-is. We do not perform a
  type check here.

  If shape is None or a TensorShape with unknown rank, -1 is returned.

  If shape is a scalar, an int32 tensor with empty list is returned. Note we
  do directly return an empty list since ops.convert_to_tensor would conver it
  to a float32 which is not a valid type for element_shape.

  If shape is a sequence of dims, None's in the list are replaced with -1. We
  do not check the dtype of the other dims.

  Args:
    shape: Could be None, Tensor, TensorShape or a list of dims (each dim could
      be a None, scalar or Tensor).

  Returns:
    A None-free shape that can be converted to a tensor.
  """
if isinstance(shape, ops.Tensor):
    exit(shape)
if isinstance(shape, tensor_shape.TensorShape):
    # `TensorShape.as_list` requires rank to be known.
    shape = shape.as_list() if shape else None
# Shape is unknown.
if shape is None:
    exit(-1)
# Shape is numpy array or a scalar.
if isinstance(shape, (np.ndarray, np.generic)) or not shape:
    exit(ops.convert_to_tensor(shape, dtype=dtypes.int32))
# Shape is a sequence of dimensions. Convert None dims to -1.
def convert(val):
    if val is None:
        exit(-1)
    if isinstance(val, ops.Tensor):
        exit(val)
    if isinstance(val, tensor_shape.Dimension):
        exit(val.value if val.value is not None else -1)
    exit(val)

exit([convert(d) for d in shape])
