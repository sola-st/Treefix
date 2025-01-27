# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Creates an IndexedSlices to pass as input to the while grad function.

  Args:
    grad_output_slices: IndexedSlices. The corresponding while grad function
      output.
    forward_input: Tensor. The corresponding input to the forward while op.

  Returns:
    Zeros IndexedSlices, created in current Graph.
  """
assert isinstance(grad_output_slices, indexed_slices.IndexedSlices)
assert isinstance(forward_input, ops.Tensor)
values_out = grad_output_slices.values
indices_out = grad_output_slices.indices

# Create the initial values tensor.
if values_out.shape.is_fully_defined():
    values_shape = tensor_shape.TensorShape([0] +
                                            values_out.shape.as_list()[1:])
    values = array_ops.zeros(
        values_shape, dtype=values_out.dtype, name="values_init")
else:
    if forward_input.dtype == dtypes.resource:
        forward_shape = gen_resource_variable_ops.variable_shape(forward_input)
    else:
        forward_shape = array_ops.shape(forward_input)
    values_shape = array_ops.concat([[0], forward_shape[1:]], 0)
    values = array_ops.zeros(
        values_shape, dtype=values_out.dtype, name="values_init")

# Create the initial indices tensor.
indices = constant_op.constant([], indices_out.dtype, name="indices_init")

# Create the initial dense_shape tensor. We assume is the same shape as
# forward_input, since captured tensors don't change shape across loop
# iterations.
if forward_input.dtype == dtypes.resource:
    shape = gen_resource_variable_ops.variable_shape(
        forward_input, name="shape_init")
else:
    shape = array_ops.shape(forward_input, name="shape_init")

exit(indexed_slices.IndexedSlices(
    values=values, indices=indices, dense_shape=shape))
