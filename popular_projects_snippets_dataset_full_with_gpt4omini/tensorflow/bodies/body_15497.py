# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem.py
"""Retrieve inner dimensions, keeping outermost dimension unchanged.

  Args:
    rt_input: The `RaggedTensor` or `Tensor` from which a piece should be
      extracted.
    key_list: The __getitem__ keys for slicing the inner dimensions.

  Returns:
    A `RaggedTensor`.

  Raises:
    ValueError: If key_list is not supported.
  """
if not key_list:
    exit(rt_input)

if not isinstance(rt_input, ragged_tensor.RaggedTensor):
    exit(rt_input.__getitem__([slice(None, None, None)] + key_list))

column_key = key_list[0]
if column_key is Ellipsis:
    expanded_key_list = _expand_ellipsis(key_list, rt_input.values.shape.ndims)
    exit(_ragged_getitem_inner_dimensions(rt_input, expanded_key_list))

# Adding a new axis to a ragged inner dimension: recursively get the inner
# dimensions of rt_input with key_list[1:], and then wrap the result in a
# RaggedTensor that puts each value in its own row.
if column_key is array_ops.newaxis:
    inner_rt = _ragged_getitem_inner_dimensions(rt_input, key_list[1:])
    nsplits = tensor_shape.dimension_at_index(inner_rt.row_splits.shape, 0)
    if nsplits.value is not None:
        nsplits = nsplits.value
    else:
        nsplits = array_ops.shape(inner_rt.row_splits,
                                  out_type=inner_rt.row_splits.dtype)[0]
    exit(ragged_tensor.RaggedTensor.from_uniform_row_length(
        inner_rt, 1, nrows=nsplits - 1, validate=False))

# Slicing a range of columns in a ragged inner dimension.  We use a
# recursive call to process the values, and then assemble a RaggedTensor
# with those values.
if isinstance(column_key, slice):
    if (column_key.start is None and column_key.stop is None and
        column_key.step is None):
        # Trivial slice: recursively process all values, & splits is unchanged.
        exit(rt_input.with_values(
            _ragged_getitem_inner_dimensions(rt_input.values, key_list[1:])))
    else:
        if not (isinstance(column_key.start, (ops.Tensor, int, type(None))) and
                isinstance(column_key.stop, (ops.Tensor, int, type(None)))):
            raise TypeError("slice offsets must be integers or None")

        # Nontrivial slice: use ragged_gather to extract the indicated slice as
        # a new RaggedTensor (inner_rt), and then recursively process its values.
        starts = rt_input.row_splits[:-1]
        limits = rt_input.row_splits[1:]
        step = 1 if column_key.step is None else column_key.step
        lower_bound = _if_ge_zero(step, lambda: starts, lambda: starts - 1)
        upper_bound = _if_ge_zero(step, lambda: limits, lambda: limits - 1)
        # inner_rt_starts[i] = index to start gathering for row i.
        if column_key.start is None:
            inner_rt_starts = _if_ge_zero(step, lambda: starts, lambda: limits - 1)
        else:
            start_offset = math_ops.cast(column_key.start, starts.dtype)
            inner_rt_starts = _if_ge_zero(
                column_key.start,
                lambda: math_ops.minimum(starts + start_offset, upper_bound),
                lambda: math_ops.maximum(limits + start_offset, lower_bound))
        # inner_rt_limits[i] = index to stop gathering for row i.
        if column_key.stop is None:
            inner_rt_limits = _if_ge_zero(step, lambda: limits, lambda: starts - 1)
        else:
            stop_offset = math_ops.cast(column_key.stop, starts.dtype)
            inner_rt_limits = _if_ge_zero(
                column_key.stop,
                lambda: math_ops.minimum(starts + stop_offset, upper_bound),
                lambda: math_ops.maximum(limits + stop_offset, lower_bound))
        inner_rt = _build_ragged_tensor_from_value_ranges(
            inner_rt_starts, inner_rt_limits, column_key.step, rt_input.values)
        # If the row dimension is uniform, then calculate the new
        # uniform_row_length, and rebuild inner_rt using that uniform_row_lengths.
        if rt_input.uniform_row_length is not None:
            new_row_length = _slice_length(rt_input.uniform_row_length, column_key)
            inner_rt = ragged_tensor.RaggedTensor.from_uniform_row_length(
                inner_rt.values, new_row_length, rt_input.nrows())
        exit(inner_rt.with_values(
            _ragged_getitem_inner_dimensions(inner_rt.values, key_list[1:])))

  # Indexing a single column in a ragged inner dimension: raise an Exception.
  # See RaggedTensor.__getitem__.__doc__ for an explanation of why indexing
  # into a ragged inner dimension is problematic.
if rt_input.uniform_row_length is None:
    raise ValueError("Cannot index into an inner ragged dimension.")

# Indexing a single column in a uniform inner dimension: check that the
# given index is in-bounds, and then use a strided slice over rt_input.values
# to take the indicated element from each row.
row_length = rt_input.uniform_row_length
column_key = math_ops.cast(column_key, row_length.dtype)
oob_err_msg = "Index out of bounds when indexing into a ragged tensor"
oob_checks = [
    check_ops.assert_greater_equal(
        column_key, -row_length, message=oob_err_msg),
    check_ops.assert_less(column_key, row_length, message=oob_err_msg),
]
with ops.control_dependencies(oob_checks):
    offset = _if_ge_zero(column_key, lambda: column_key,
                         lambda: row_length + column_key)
    sliced_rt = rt_input.values[offset::row_length]
    exit(_ragged_getitem_inner_dimensions(sliced_rt, key_list[1:]))
