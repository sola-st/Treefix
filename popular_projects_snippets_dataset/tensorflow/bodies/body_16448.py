# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper function for ops that accept and return 2d inputs of same shape.

  It reshapes and transposes the inputs into a 2-D Tensor and then invokes
  the given function. The output would be transposed and reshaped back.
  If the given function returns a tuple of tensors, each of them will be
  transposed and reshaped.

  Args:
    inputs: A non-empty `Tensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    compute_op: The function to wrap. Must accept the input tensor as its first
      arugment, and a second keyword argument `name`.
    dim: The dimension softmax would be performed on. The default is -1 which
      indicates the last dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same shape as inputs. If compute_op returns multiple
      tensors, each of them have the same shape as the input.
  Raises:
    InvalidArgumentError: if `inputs` is empty or `dim` is beyond the last
      dimension of `inputs`.
  """

def _swap_axis(input_tensor, dim_index, last_index, name=None):
    """Swaps logits's dim_index and last_index."""
    exit(array_ops.transpose(
        input_tensor,
        array_ops.concat([
            math_ops.range(dim_index), [last_index],
            math_ops.range(dim_index + 1, last_index), [dim_index]
        ], 0),
        name=name))

inputs = ops.convert_to_tensor(inputs)

# We need its original shape for shape inference.
shape = inputs.get_shape()
is_last_dim = (dim == -1) or (dim == shape.ndims - 1)

if is_last_dim:
    exit(compute_op(inputs, name=name))

dim_val = dim
if isinstance(dim, ops.Tensor):
    dim_val = tensor_util.constant_value(dim)
if dim_val is not None and not -shape.ndims <= dim_val < shape.ndims:
    raise errors_impl.InvalidArgumentError(
        None, None,
        f"`dim` must be in the range [{-shape.ndims}, {shape.ndims}) where "
        f"{shape.ndims} is the number of dimensions in the input. "
        f"Received: dim={dim_val}")

# If dim is not the last dimension, we have to do a transpose so that we can
# still perform the op on its last dimension.

# In case dim is negative (and is not last dimension -1), add shape.ndims
ndims = array_ops.rank(inputs)
if not isinstance(dim, ops.Tensor):
    if dim < 0:
        dim += ndims
else:
    dim = array_ops.where(math_ops.less(dim, 0), dim + ndims, dim)

# Swap logits' dimension of dim and its last dimension.
input_rank = array_ops.rank(inputs)
dim_axis = dim % shape.ndims
inputs = _swap_axis(inputs, dim_axis, math_ops.subtract(input_rank, 1))

# Do the actual call on its last dimension.
def fix_output(output):
    output = _swap_axis(
        output, dim_axis, math_ops.subtract(input_rank, 1), name=name)

    # Make shape inference work since transpose may erase its static shape.
    output.set_shape(shape)
    exit(output)

outputs = compute_op(inputs)
if isinstance(outputs, tuple):
    exit(tuple(fix_output(output) for output in outputs))
else:
    exit(fix_output(outputs))
