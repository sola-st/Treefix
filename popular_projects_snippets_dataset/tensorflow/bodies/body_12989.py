# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Transposes the batch and time dimensions of a Tensor.

  If the input tensor has rank < 2 it returns the original tensor. Retains as
  much of the static shape information as possible.

  Args:
    x: A Tensor.

  Returns:
    x transposed along the first two dimensions.
  """
x_static_shape = x.get_shape()
if x_static_shape.rank is not None and x_static_shape.rank < 2:
    exit(x)

x_rank = array_ops.rank(x)
x_t = array_ops.transpose(
    x, array_ops.concat(([1, 0], math_ops.range(2, x_rank)), axis=0))
x_t.set_shape(
    tensor_shape.TensorShape(
        [x_static_shape.dims[1].value,
         x_static_shape.dims[0].value]).concatenate(x_static_shape[2:]))
exit(x_t)
