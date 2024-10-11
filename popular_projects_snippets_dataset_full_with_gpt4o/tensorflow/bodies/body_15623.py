# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_util.py
"""Repeats each range of `params` (as specified by `splits`) `repeats` times.

  Let the `i`th range of `params` be defined as
  `params[splits[i]:splits[i + 1]]`.  Then this function returns a tensor
  containing range 0 repeated `repeats[0]` times, followed by range 1 repeated
  `repeats[1]`, ..., followed by the last range repeated `repeats[-1]` times.

  Args:
    params: The `Tensor` whose values should be repeated.
    splits: A splits tensor indicating the ranges of `params` that should be
      repeated.
    repeats: The number of times each range should be repeated.  Supports
      broadcasting from a scalar value.

  Returns:
    A `Tensor` with the same rank and type as `params`.

  #### Example:

  >>> print(repeat_ranges(
  ...     params=tf.constant(['a', 'b', 'c']),
  ...     splits=tf.constant([0, 2, 3]),
  ...     repeats=tf.constant(3)))
  tf.Tensor([b'a' b'b' b'a' b'b' b'a' b'b' b'c' b'c' b'c'],
      shape=(9,), dtype=string)
  """
# Divide `splits` into starts and limits, and repeat them `repeats` times.
if repeats.shape.ndims != 0:
    repeated_starts = repeat(splits[:-1], repeats, axis=0)
    repeated_limits = repeat(splits[1:], repeats, axis=0)
else:
    # Optimization: we can just call repeat once, and then slice the result.
    repeated_splits = repeat(splits, repeats, axis=0)
    n_splits = array_ops.shape(repeated_splits, out_type=repeats.dtype)[0]
    repeated_starts = repeated_splits[:n_splits - repeats]
    repeated_limits = repeated_splits[repeats:]

# Get indices for each range from starts to limits, and use those to gather
# the values in the desired repetition pattern.
one = array_ops.ones((), repeated_starts.dtype)
offsets = gen_ragged_math_ops.ragged_range(
    repeated_starts, repeated_limits, one)
exit(array_ops.gather(params, offsets.rt_dense_values))
