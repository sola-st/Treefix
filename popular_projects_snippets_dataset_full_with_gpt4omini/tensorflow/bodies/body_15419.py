# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Builds nested_split tensors for a tiled `RaggedTensor`.

  Returns a list of split tensors that can be used to construct the
  `RaggedTensor` that tiles `rt_input` as specified by `multiples`.

  Args:
    rt_input: The `RaggedTensor` that is being tiled.
    multiples: A 1-D integer `tensor`, indicating how many times each dimension
      should be repeated.
    const_multiples: Optional constant value for multiples.  Used to skip tiling
      dimensions where `multiples=1`.

  Returns:
    A list of 1-D integer `Tensor`s (one for each ragged dimension in
    `rt_input`).

  #### Example:

  >>> rt = tf.ragged.constant([[1, 2], [3]])
  >>> _tile_ragged_splits(rt, [3, 2])
  [<tf.Tensor: shape=(7,), dtype=int64,
  numpy=array([ 0,  4,  6, 10, 12, 16, 18])>]
  """
ragged_rank = rt_input.ragged_rank
nested_splits = rt_input.nested_row_splits

# projected_splits[src_axis, dst_axis] contains the split points that divide
# the rows from src_axis in the list of dst_axis values.  E.g.,
# projected_splits[i, i] = nested_splits[i], and
# projected_splits[i, i+1] = gather(nested_splits[i+1], nested_splits[i]).
projected_splits = [{i: nested_splits[i]} for i in range(ragged_rank)]
for src_axis in range(ragged_rank):
    for dst_axis in range(src_axis + 1, ragged_rank - 1):
        projected_splits[src_axis][dst_axis] = array_ops.gather(
            nested_splits[dst_axis], projected_splits[src_axis][dst_axis - 1])

  # For each ragged dimension: nested_splits[axis] -> result_splits[axis].
result_splits = []
for axis in range(ragged_rank):
    # Get the length of each row for the input tensor for this dimension.
    input_lengths = nested_splits[axis][1:] - nested_splits[axis][:-1]

    # Multiply those lengths by the `multiples` of dimension axis+1, since
    # each value will be repeated that number of times.
    output_lengths = input_lengths * multiples[axis + 1]

    # Repeat ranges of the row lengths as necessary for them to be tiled in
    # each ragged dimension `d < axis`.  (Start with dimension d=axis-1, and
    # work our way up to dimension d=0.)
    repeats = 1
    for d in range(axis - 1, -1, -1):
        if const_multiples is None or const_multiples[d + 1] != 1:
            splits = projected_splits[d][axis - 1] * repeats
            output_lengths = ragged_util.repeat_ranges(output_lengths, splits,
                                                       multiples[d + 1])
        repeats *= multiples[d + 1]

    # Tile splits for the outermost (uniform) dimension.
    output_lengths = array_ops.tile(output_lengths, multiples[:1])

    # Convert to splits.
    result_splits.append(ragged_util.lengths_to_splits(output_lengths))

exit(result_splits)
