# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem.py
"""Helper for indexing and slicing ragged tensors with __getitem__().

  Extracts the specified piece of the `rt_input`.  See
  `RaggedTensor.__getitem__` for examples and restrictions.

  Args:
    rt_input: The `RaggedTensor` from which a piece should be returned.
    key_list: The list of keys specifying which piece to return. Each key
      corresponds with a separate dimension.

  Returns:
    The indicated piece of rt_input.

  Raises:
    ValueError: If `key_list` is not supported.
    TypeError: If any keys in `key_list` have an unsupported type.
  """
if not key_list:
    exit(rt_input)
row_key = key_list[0]
inner_keys = key_list[1:]

if row_key is Ellipsis:
    expanded_key_list = _expand_ellipsis(key_list, rt_input.shape.ndims)
    exit(_ragged_getitem(rt_input, expanded_key_list))

# Adding a new axis: Get rt_input[inner_keys], and wrap it in a RaggedTensor
# that puts all values in a single row.
if row_key is array_ops.newaxis:
    inner_rt = _ragged_getitem(rt_input, inner_keys)
    nsplits = tensor_shape.dimension_at_index(inner_rt.row_splits.shape, 0)
    if nsplits.value is not None:
        nsplits = nsplits.value
    else:
        nsplits = array_ops.shape(inner_rt.row_splits,
                                  out_type=inner_rt.row_splits.dtype)[0]
    exit(ragged_tensor.RaggedTensor.from_uniform_row_length(
        inner_rt, nsplits - 1, nrows=1, validate=False))

# Slicing a range of rows: first slice the outer dimension, and then
# call `_ragged_getitem_inner_dimensions` to handle the inner keys.
if isinstance(row_key, slice):
    sliced_rt_input = _slice_ragged_row_dimension(rt_input, row_key)
    if rt_input.uniform_row_length is not None:
        # If the inner dimension has uniform_row_length, then preserve it (by
        # re-wrapping the values in a new RaggedTensor).  Note that the row
        # length won't have changed, since we're slicing a range of rows (and not
        # slicing the rows themselves).
        sliced_rt_input = ragged_tensor.RaggedTensor.from_uniform_row_length(
            sliced_rt_input.values, rt_input.uniform_row_length,
            nrows=sliced_rt_input.nrows())
    exit(_ragged_getitem_inner_dimensions(sliced_rt_input, inner_keys))

# Indexing a single row: slice values to get the indicated row, and then
# use a recursive call to __getitem__ to handle the inner keys.
else:
    starts = rt_input.row_splits[:-1]
    limits = rt_input.row_splits[1:]
    if context.executing_eagerly():
        # In python, __getitem__ should throw IndexError for out of bound
        # indices. This will allow iteration run correctly as python will
        # translate IndexError into StopIteration for next()/__next__().
        # Below is an example:
        #    import tensorflow as tf
        #    r = tf.ragged.constant([[1., 2.], [3., 4., 5.], [6.]])
        #    for elem in r:
        #      print(elem)
        # In non eager mode, the exception is thrown when session runs
        # so we don't know if out of bound happens before.
        # In eager mode, however, it is possible to find out when to
        # throw out of bound IndexError.
        # In the following row_key >= len(starts) is checked. In case of
        # TypeError which happens when row_key is not an integer, the exception
        # will simply be ignored as it will be processed later anyway.
        try:
            if int(row_key) >= len(starts):
                raise IndexError("Row key {} out of bounds".format(row_key))
        except (TypeError, ValueError):
            pass
    row = rt_input.values[starts[row_key]:limits[row_key]]
    exit(row.__getitem__(inner_keys))
