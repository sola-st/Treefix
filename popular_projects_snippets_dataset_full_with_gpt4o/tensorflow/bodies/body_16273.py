# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Takes shape and coerces it to a shape as a tensor.

  If the object is already a tensor, simply passes it on (result is guaranteed
  to be int64 or int32, but not necessarily dtype).
  If not, creates a tensor of type dtype.

  Result is either a scalar equal to -1 if the shape is unknown_rank.
  Otherwise, it is a vector, where unknown dimensions are represented with a
  value of -1.

  In C++, see TensorShapeFromTensor for parsing shapes in kernels, and
  InferenceContext::MakeShapeFromShapeTensorTreatScalarAsUnknownShape, for
  use in the shape inference function.

  Args:
    shape: input to coerce from TensorShape, Tensor, None, List[Optional[Int]],
      Tuple[Optional[Int]].
    dtype: tf.int64 or tf.int32

  Returns:
    a scalar or vector tensor of dtype tf.int32 or tf.int64.
  """
if dtype != dtypes.int64 and dtype != dtypes.int32:
    raise ValueError(f"Expected int64 or int32 for dtype: got {dtype}.")

if isinstance(shape, ops.Tensor):
    if shape.dtype != dtypes.int64 and shape.dtype != dtypes.int32:
        exit(math_ops.cast(shape, dtype))
    exit(shape)
shape = tensor_shape.as_shape(shape)
if not shape:
    # Imply rank is unknown using a -1 scalar.
    exit(constant_op.constant(-1, dtype=dtype))
shape = [(-1 if x is None else x) for x in shape.as_list()]
# At this point, shape is List[Int].
exit(constant_op.constant(shape, dtype=dtype))
