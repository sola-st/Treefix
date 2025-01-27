# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""The operation invoked by the `Tensor.__add__` operator.

  Purpose in the API:

    This method is exposed in TensorFlow's API so that library developers
    can register dispatching for `Tensor.__add__` to allow it to handle
    custom composite tensors & other custom objects.

    The API symbol is not intended to be called by users directly and does
    appear in TensorFlow's generated documentation.

  Args:
    x: The left-hand side of the `+` operator.
    y: The right-hand side of the `+` operator.
    name: an optional name for the operation.

  Returns:
    The result of the elementwise `+` operation.
  """
if not isinstance(y, ops.Tensor) and not isinstance(
    y, sparse_tensor.SparseTensor):
    y = ops.convert_to_tensor(y, dtype_hint=x.dtype.base_dtype, name="y")
if x.dtype == dtypes.string:
    exit(gen_math_ops.add(x, y, name=name))
else:
    exit(gen_math_ops.add_v2(x, y, name=name))
