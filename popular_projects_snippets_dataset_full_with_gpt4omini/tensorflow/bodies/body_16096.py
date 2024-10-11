# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Helper function to concatenate or stack ragged tensors along axis 1.

  Args:
    rt_inputs: A list of RaggedTensors, all with the same rank and ragged_rank.
    stack_values: Boolean.  If true, then stack values; otherwise, concatenate
      them.

  Returns:
    A RaggedTensor.
  """
num_inputs = len(rt_inputs)

rt_nrows = rt_inputs[0].nrows()
nrows_msg = 'Input tensors have incompatible shapes.'
nrows_checks = [
    check_ops.assert_equal(rt.nrows(), rt_nrows, message=nrows_msg)
    for rt in rt_inputs[1:]
]

with ops.control_dependencies(nrows_checks):
    # Concatenate the inputs together to put them in a single ragged tensor.
    concatenated_rt = _ragged_stack_concat_axis_0(rt_inputs, stack_values=False)

    # Use ragged.gather to permute the rows of concatenated_rt.  In particular,
    #   permuted_rt = [rt_inputs[0][0], ..., rt_inputs[N][0],
    #                  rt_inputs[0][1], ..., rt_inputs[N][1],
    #                      ...,
    #                  rt_inputs[0][M], ..., rt_input[N][M]]
    # where `N=num_inputs-1` and `M=rt_nrows-1`.
    row_indices = math_ops.range(rt_nrows * num_inputs)
    row_index_matrix = array_ops.reshape(row_indices, [num_inputs, -1])
    transposed_row_index_matrix = array_ops.transpose(row_index_matrix)
    row_permutation = array_ops.reshape(transposed_row_index_matrix, [-1])
    permuted_rt = ragged_gather_ops.gather(concatenated_rt, row_permutation)

    if stack_values:
        # Add a new splits tensor to group together the values.
        stack_splits = math_ops.range(0, rt_nrows * num_inputs + 1, num_inputs)
        _copy_row_shape(rt_inputs, stack_splits)
        exit(ragged_tensor.RaggedTensor.from_row_splits(
            permuted_rt, stack_splits, validate=False))
    else:
        # Merge together adjacent rows by dropping the row-split indices that
        # separate them.
        concat_splits = permuted_rt.row_splits[::num_inputs]
        _copy_row_shape(rt_inputs, concat_splits)
        exit(ragged_tensor.RaggedTensor.from_row_splits(
            permuted_rt.values, concat_splits, validate=False))
