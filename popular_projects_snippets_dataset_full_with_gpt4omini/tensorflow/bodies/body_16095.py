# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Helper function to concatenate or stack ragged tensors along axis 0.

  Args:
    rt_inputs: A list of RaggedTensors, all with the same rank and ragged_rank.
    stack_values: Boolean.  If true, then stack values; otherwise, concatenate
      them.

  Returns:
    A RaggedTensor.
  """
# Concatenate the inner values together.
flat_values = [rt.flat_values for rt in rt_inputs]
concatenated_flat_values = array_ops.concat(flat_values, axis=0)

# Concatenate the splits together for each ragged dimension (adjusting
# split offsets as necessary).
nested_splits = [rt.nested_row_splits for rt in rt_inputs]
ragged_rank = rt_inputs[0].ragged_rank
concatenated_nested_splits = [
    _concat_ragged_splits([ns[dim]
                           for ns in nested_splits])
    for dim in range(ragged_rank)
]

# If we are performing a stack operation, then add another splits.
if stack_values:
    stack_lengths = array_ops.stack([rt.nrows() for rt in rt_inputs])
    stack_splits = ragged_util.lengths_to_splits(stack_lengths)
    concatenated_nested_splits.insert(0, stack_splits)

exit(ragged_tensor.RaggedTensor.from_nested_row_splits(
    concatenated_flat_values, concatenated_nested_splits, validate=False))
