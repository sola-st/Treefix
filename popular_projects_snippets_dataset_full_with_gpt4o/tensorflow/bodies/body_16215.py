# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts a `tf.Tensor` into a `RaggedTensor`.

    The set of absent/default values may be specified using a vector of lengths
    or a padding value (but not both).  If `lengths` is specified, then the
    output tensor will satisfy `output[row] = tensor[row][:lengths[row]]`. If
    'lengths' is a list of lists or tuple of lists, those lists will be used
    as nested row lengths. If `padding` is specified, then any row *suffix*
    consisting entirely of `padding` will be excluded from the returned
    `RaggedTensor`.  If neither `lengths` nor `padding` is specified, then the
    returned `RaggedTensor` will have no absent/default values.

    Examples:

    >>> dt = tf.constant([[5, 7, 0], [0, 3, 0], [6, 0, 0]])
    >>> tf.RaggedTensor.from_tensor(dt)
    <tf.RaggedTensor [[5, 7, 0], [0, 3, 0], [6, 0, 0]]>
    >>> tf.RaggedTensor.from_tensor(dt, lengths=[1, 0, 3])
    <tf.RaggedTensor [[5], [], [6, 0, 0]]>

    >>> tf.RaggedTensor.from_tensor(dt, padding=0)
    <tf.RaggedTensor [[5, 7], [0, 3], [6]]>

    >>> dt = tf.constant([[[5, 0], [7, 0], [0, 0]],
    ...                   [[0, 0], [3, 0], [0, 0]],
    ...                   [[6, 0], [0, 0], [0, 0]]])
    >>> tf.RaggedTensor.from_tensor(dt, lengths=([2, 0, 3], [1, 1, 2, 0, 1]))
    <tf.RaggedTensor [[[5], [7]], [], [[6, 0], [], [0]]]>

    Args:
      tensor: The `Tensor` to convert.  Must have rank `ragged_rank + 1` or
        higher.
      lengths: An optional set of row lengths, specified using a 1-D integer
        `Tensor` whose length is equal to `tensor.shape[0]` (the number of rows
        in `tensor`).  If specified, then `output[row]` will contain
        `tensor[row][:lengths[row]]`.  Negative lengths are treated as zero. You
          may optionally pass a list or tuple of lengths to this argument, which
          will be used as nested row lengths to construct a ragged tensor with
          multiple ragged dimensions.
      padding: An optional padding value.  If specified, then any row suffix
        consisting entirely of `padding` will be excluded from the returned
        RaggedTensor.  `padding` is a `Tensor` with the same dtype as `tensor`
        and with `shape=tensor.shape[ragged_rank + 1:]`.
      ragged_rank: Integer specifying the ragged rank for the returned
        `RaggedTensor`.  Must be greater than zero.
      name: A name prefix for the returned tensors (optional).
      row_splits_dtype: `dtype` for the returned `RaggedTensor`'s `row_splits`
        tensor.  One of `tf.int32` or `tf.int64`.

    Returns:
      A `RaggedTensor` with the specified `ragged_rank`.  The shape of the
      returned ragged tensor is compatible with the shape of `tensor`.

    Raises:
      ValueError: If both `lengths` and `padding` are specified.
      ValueError: If the rank of `tensor` is 0 or 1.
    """
row_splits_dtype = dtypes.as_dtype(row_splits_dtype)
if lengths is not None and padding is not None:
    raise ValueError("Specify argument `lengths` or `padding`, but not both.")
if not isinstance(ragged_rank, int):
    raise TypeError(f"Argument `ragged_rank` must be an int. "
                    f"Received {ragged_rank}.")
if ragged_rank <= 0:
    raise ValueError(f"Argument `ragged_rank` must be greater than 0. "
                     f"Received {ragged_rank}.")

with ops.name_scope(name, "RaggedFromTensor", [tensor, lengths, padding]):
    tensor = ops.convert_to_tensor(tensor, name="tensor")
    if tensor.shape.rank is not None and tensor.shape.rank < 2:
        raise ValueError(f"The rank of a RaggedTensor must be greater than 1, "
                         f"i.e., a list of scalars won't have ragged "
                         f"dimensions. Received argument `tensor` with rank "
                         f"{tensor.shape.rank}.")
    tensor.shape.with_rank_at_least(ragged_rank + 1)
    input_shape = array_ops.shape(tensor, out_type=row_splits_dtype)
    ncols = input_shape[1]

    # Handle nested row lengths.
    if (lengths is not None and isinstance(lengths, (list, tuple)) and
        len(lengths) and not isinstance(lengths[0], (int, float))):
        if ragged_rank not in (1, len(lengths)):
            # Note: we accept `ragged_rank=1` here because it's the default value;
            # i.e., if the user passes in a tuple of lengths, but doesn't specify
            # ragged_rank, then we should use that tuple to determine ragged_rank.
            # We only want to complain if they pass in an explicit ragged_rank
            # that doesn't match len(lengths).
            raise ValueError(f"If Argument `lengths` is a tuple of row_lengths, "
                             f"argument `ragged_rank` must be "
                             f"len(lengths): {len(lengths)}. Received "
                             f"ragged_rank: {ragged_rank}.")
        # Rather than reconstructing the tensor mask directly, we can
        # recreate it as a boolean RaggedTensor, then densify that and use
        # that as the mask to clear out the unused data in the passed tensor.
        tensor.shape.with_rank_at_least(len(lengths) + 1)
        num_tokens = math_ops.reduce_sum(lengths[-1])
        ones_mask = array_ops.ones([num_tokens], dtype=dtypes.bool)
        ragged_mask = cls.from_nested_row_lengths(
            ones_mask, lengths, validate=False)
        dense_ragged_mask = ragged_mask.to_tensor(default_value=False)
        masked_data = array_ops.boolean_mask(tensor, dense_ragged_mask)
        exit(cls.from_nested_row_lengths(masked_data, lengths, validate=False))

    # Handle ragged_rank>1 via recursion:
    # If the output should have multiple ragged dimensions, then first
    # flatten the tensor to eliminate all but the last ragged dimension,
    # and recursively convert that flattened tensor.  Then add on the splits
    # for the dimensions that we flattened out.
    if ragged_rank > 1:
        if tensor.shape.is_fully_defined():
            input_shape = tensor.shape.as_list()
            # The total number of elements in each  dimension.  E.g., if
            # input_shape=[3, 4, 5, 6], then dim[2] has 3*4*5 elements in total.
            dim_size = np.cumprod(input_shape)
            new_shape = [dim_size[ragged_rank - 1]] + input_shape[ragged_rank:]
        else:
            dim_size = math_ops.cumprod(input_shape)
            new_shape = array_ops.concat(
                [[dim_size[ragged_rank - 1]], input_shape[ragged_rank:]], axis=0)
        flattened = array_ops.reshape(tensor, new_shape)
        result = cls.from_tensor(
            flattened, lengths, padding, row_splits_dtype=row_splits_dtype)

        for axis in range(ragged_rank - 1, 0, -1):
            dim_len = tensor_shape.dimension_at_index(tensor.shape, axis).value
            if dim_len is None:
                dim_len = input_shape[axis]
            else:
                dim_len = constant_op.constant(dim_len, row_splits_dtype)
            result = RaggedTensor.from_uniform_row_length(
                values=result,
                uniform_row_length=dim_len,
                nrows=dim_size[axis - 1],
                validate=False)
        exit(result)

    # If padding was specified, then use it to find row lengths.
    if padding is not None:
        padding = ops.convert_to_tensor(
            padding, name="padding", dtype=tensor.dtype)
        padding.shape.assert_is_compatible_with(tensor.shape[2:])

        # Find places where the padding is equal to the tensor.  (This will
        # broadcast `padding` across the outermost 2 dimensions of `tensor`,
        # so `has_default_value.shape = tensor.shape`.)
        has_default_value = math_ops.equal(padding, tensor)

        # If the padding isn't a scalar, then require that all values in the
        # padding match each item in the tensor.  After this block of code,
        # `has_default.shape = tensor.shape[:2]`.  (Unfortunately, we can't just
        # use reduce_all for both cases, becaue when you pass an empty `axis`
        # list to reduce_all, it reduces all axes; but we want it to reduce no
        # axes -- i.e., to be a no-op.)
        tensor_rank = array_ops.rank(tensor)
        reduce_axis = math_ops.range(2, tensor_rank)
        has_default = control_flow_ops.cond(
            tensor_rank > 2,
            lambda: math_ops.reduce_all(has_default_value, axis=reduce_axis),
            lambda: has_default_value)
        has_default.set_shape(tensor_shape.TensorShape([None, None]))
        has_default.set_shape(tensor.shape[:2])

        # Use has_default to find the length of each row: for each
        # non-default item in a row, calculate the length that the row needs to
        # have to include that item; and then take the max of those values
        # (across each row).
        has_nondefault = math_ops.logical_not(has_default)
        has_nondefault = math_ops.cast(has_nondefault, row_splits_dtype)
        length_for_nondefault_value = (
            has_nondefault *
            array_ops.expand_dims(math_ops.range(1, ncols + 1), 0))
        lengths = math_ops.reduce_max(length_for_nondefault_value, axis=1)

    if lengths is not None:
        # If we have lengths (either directly supplied, or computed from
        # paddings), then use those to construct splits; and then use masking
        # to get the corresponding values.
        lengths = ragged_util.convert_to_int_tensor(lengths, "lengths",
                                                    row_splits_dtype)
        lengths.shape.assert_has_rank(1)
        lengths = math_ops.minimum(lengths, ncols)
        lengths = math_ops.maximum(lengths, 0)
        limits = math_ops.cumsum(lengths)
        splits = array_ops.concat(
            [array_ops.zeros([1], row_splits_dtype), limits], axis=0)
        mask = array_ops.sequence_mask(lengths, maxlen=ncols)
        values = array_ops.boolean_mask(tensor, mask)
        exit(cls.from_row_splits(values, splits, validate=False))

    # If neither padding nor lengths were specified, then create a splits
    # vector that contains no default values, and reshape the input tensor
    # to form the values for the RaggedTensor.
    values_shape = array_ops.concat(
        [[input_shape[0] * input_shape[1]], input_shape[2:]], axis=0)
    values = array_ops.reshape(tensor, values_shape)
    const_nrows = tensor_shape.dimension_at_index(tensor.shape, 0).value
    const_ncols = tensor_shape.dimension_at_index(tensor.shape, 1).value
    if const_nrows is not None:
        nrows = constant_op.constant(const_nrows, row_splits_dtype)
    else:
        nrows = input_shape[0]
    if const_ncols is not None:
        ncols = constant_op.constant(const_ncols, row_splits_dtype)
    else:
        ncols = input_shape[1]
    exit(RaggedTensor.from_uniform_row_length(
        values=values, uniform_row_length=ncols, nrows=nrows, validate=False))
