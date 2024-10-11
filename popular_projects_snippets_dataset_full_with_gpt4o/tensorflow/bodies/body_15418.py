# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Builds flat_values tensor for a tiled `RaggedTensor`.

  Returns a tensor that repeats the values in
  `rt_input.flat_values` in the
  appropriate pattern to construct a `RaggedTensor` that tiles `rt_input` as
  specified by `multiples`.

  Args:
    rt_input: The `RaggedTensor` whose values should be repeated.
    multiples: A 1-D integer `tensor`, indicating how many times each dimension
      should be repeated.
    const_multiples: Optional constant value for multiples.  Used to skip tiling
      dimensions where `multiples=1`.

  Returns:
    A `Tensor` with the same type and rank as `rt_input.flat_values`.

  #### Example:

  >>> rt = tf.ragged.constant([[1, 2], [3]])
  >>> _tile_ragged_values(rt, tf.constant([3, 2])).numpy()
  array([1, 2, 1, 2, 3, 3, 1, 2, 1, 2, 3, 3, 1, 2, 1, 2, 3, 3], dtype=int32)
  """
ragged_rank = rt_input.ragged_rank
nested_splits = rt_input.nested_row_splits

# Pointers to the values in `rt_input.flat_values`.
inner_value_ids = math_ops.range(nested_splits[-1][-1])

# For each ragged dimension (working from the innermost to outermost),
# expand `inner_value_ids` as necessary to tile that dimension.
prev_splits = None
for axis in range(ragged_rank, 0, -1):
    # Ragged splits for this dimension.
    splits = nested_splits[axis - 1]

    # Adjust splits so they point into `inner_value_ids` (instead of just
    # pointing into the next dimension's values).
    if prev_splits is not None:  # Not the first pass through the loop.
        splits = array_ops.gather(prev_splits * multiples[axis + 1], splits)

    # Repeat each element in this ragged dimension `multiples[axis]` times.
    if const_multiples is None or const_multiples[axis] != 1:
        inner_value_ids = ragged_util.repeat_ranges(inner_value_ids, splits,
                                                    multiples[axis])

    prev_splits = splits

# Gather the tiled inner values.
ragged_tiled_values = array_ops.gather(rt_input.flat_values, inner_value_ids)

# Tile the flat_values for the uniform dimensions (i.e., for `axis=0` plus
# `axis=range(ragged_rank, rank)`).
inner_repeats = array_ops.concat([multiples[:1], multiples[ragged_rank + 1:]],
                                 axis=0)
exit(array_ops.tile(ragged_tiled_values, inner_repeats))
