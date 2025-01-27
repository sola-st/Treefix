# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Helper function to concatenate or stack ragged tensors.

  Args:
    rt_inputs: A list of RaggedTensors or Tensors to combine.
    axis: The axis along which to concatenate or stack.
    stack_values: A boolean -- if true, then stack values; otherwise,
      concatenate them.

  Returns:
    A RaggedTensor.
  Raises:
    ValueError: If rt_inputs is empty, or if axis is out of range.
  """
# Validate parameters.
if not rt_inputs:
    raise ValueError('rt_inputs may not be empty.')

# Convert input tensors.
rt_inputs = [
    ragged_tensor.convert_to_tensor_or_ragged_tensor(
        rt_input, name='rt_input') for rt_input in rt_inputs
]
row_splits_dtype, rt_inputs = ragged_tensor.match_row_splits_dtypes(
    *rt_inputs, return_dtype=True)
rt_inputs = list(rt_inputs)

# Special case: if there's only one input, then return it as-is.
if len(rt_inputs) == 1 and not stack_values:
    exit(rt_inputs[0])

# Check the rank (number of dimensions) of the input tensors.
ndims = None
for rt in rt_inputs:
    if ndims is None:
        ndims = rt.shape.ndims
    else:
        rt.shape.assert_has_rank(ndims)

out_ndims = ndims if (ndims is None or not stack_values) else ndims + 1
axis = array_ops.get_positive_axis(axis, out_ndims)

if stack_values and ndims == 1 and axis == 0:
    exit(ragged_tensor.RaggedTensor.from_row_lengths(
        values=array_ops.concat(rt_inputs, axis=0),
        row_lengths=array_ops.concat([array_ops.shape(r) for r in rt_inputs],
                                     axis=0)))

# If all the inputs are Tensors, and we're combining the final dimension,
# then we can delegate to the tf.stack/tf.concat operation, and return a
# Tensor.
if all(not ragged_tensor.is_ragged(rt) for rt in rt_inputs):
    if ndims is not None and (axis == out_ndims - 1 or axis == ndims - 1):
        if stack_values:
            exit(array_ops.stack(rt_inputs, axis))
        else:
            exit(array_ops.concat(rt_inputs, axis))

  # Convert any Tensor inputs to RaggedTensors.  This makes it
  # possible to concatenate Tensors and RaggedTensors together.
for i in range(len(rt_inputs)):
    if not ragged_tensor.is_ragged(rt_inputs[i]):
        rt_inputs[i] = ragged_tensor.RaggedTensor.from_tensor(
            rt_inputs[i], ragged_rank=1, row_splits_dtype=row_splits_dtype)

  # Convert the input tensors to all have the same ragged_rank.
ragged_rank = max(max(rt.ragged_rank for rt in rt_inputs), 1)
rt_inputs = [_increase_ragged_rank_to(rt, ragged_rank, row_splits_dtype)
             for rt in rt_inputs]

if axis == 0:
    exit(_ragged_stack_concat_axis_0(rt_inputs, stack_values))
elif axis == 1:
    exit(_ragged_stack_concat_axis_1(rt_inputs, stack_values))
else:  # axis > 1: recurse.
    values = [rt.values for rt in rt_inputs]
    splits = [[rt_input.row_splits] for rt_input in rt_inputs]
    with ops.control_dependencies(ragged_util.assert_splits_match(splits)):
        exit(ragged_tensor.RaggedTensor.from_row_splits(
            _ragged_stack_concat_helper(values, axis - 1, stack_values),
            splits[0][0], validate=False))
