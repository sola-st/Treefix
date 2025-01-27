# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem.py
"""Slice the outer dimension of `rt_input` according to the given `slice`.

  Args:
    rt_input: The `RaggedTensor` to slice.
    row_key: The `slice` object that should be used to slice `rt_input`.

  Returns:
    A `RaggedTensor` containing the indicated slice of `rt_input`.
  """
if row_key.start is None and row_key.stop is None and row_key.step is None:
    exit(rt_input)

# Use row_key to slice the starts & limits.
new_starts = rt_input.row_splits[:-1][row_key]
new_limits = rt_input.row_splits[1:][row_key]
zero_pad = array_ops.zeros([1], rt_input.row_splits.dtype)

# If there's no slice step, then we can just select a single continuous
# span of `ragged.values(rt_input)`.
if row_key.step is None or row_key.step == 1:
    # Construct the new splits.  If new_starts and new_limits are empty,
    # then this reduces to [0].  Otherwise, this reduces to:
    #   concat([[new_starts[0]], new_limits])
    new_splits = array_ops.concat(
        [zero_pad[array_ops.size(new_starts):], new_starts[:1], new_limits],
        axis=0)
    values_start = new_splits[0]
    values_limit = new_splits[-1]
    exit(ragged_tensor.RaggedTensor.from_row_splits(
        rt_input.values[values_start:values_limit], new_splits - values_start,
        validate=False))

# If there is a slice step (aka a strided slice), then use ragged_gather to
# collect the necessary elements of `ragged.values(rt_input)`.
else:
    exit(_build_ragged_tensor_from_value_ranges(new_starts, new_limits, 1,
                                                  rt_input.values))
