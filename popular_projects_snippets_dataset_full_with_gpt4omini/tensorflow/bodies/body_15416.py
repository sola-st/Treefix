# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Applies a boolean mask to `data` without flattening the mask dimensions.

  Returns a potentially ragged tensor that is formed by retaining the elements
  in `data` where the corresponding value in `mask` is `True`.

  * `output[a1...aA, i, b1...bB] = data[a1...aA, j, b1...bB]`

     Where `j` is the `i`th `True` entry of `mask[a1...aA]`.

  Note that `output` preserves the mask dimensions `a1...aA`; this differs
  from `tf.boolean_mask`, which flattens those dimensions.

  Args:
    data: A potentially ragged tensor.
    mask: A potentially ragged boolean tensor.  `mask`'s shape must be a prefix
      of `data`'s shape.  `rank(mask)` must be known statically.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A potentially ragged tensor that is formed by retaining the elements in
    `data` where the corresponding value in `mask` is `True`.

    * `rank(output) = rank(data)`.
    * `output.ragged_rank = max(data.ragged_rank, rank(mask) - 1)`.

  Raises:
    ValueError: if `rank(mask)` is not known statically; or if `mask.shape` is
      not a prefix of `data.shape`.

  #### Examples:

  >>> # Aliases for True & False so data and mask line up.
  >>> T, F = (True, False)

  >>> tf.ragged.boolean_mask(  # Mask a 2D Tensor.
  ...     data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  ...     mask=[[T, F, T], [F, F, F], [T, F, F]]).to_list()
  [[1, 3], [], [7]]

  >>> tf.ragged.boolean_mask(  # Mask a 2D RaggedTensor.
  ...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
  ...     tf.ragged.constant([[F, F, T], [F], [T, T]])).to_list()
  [[3], [], [5, 6]]

  >>> tf.ragged.boolean_mask(  # Mask rows of a 2D RaggedTensor.
  ...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
  ...     tf.ragged.constant([True, False, True])).to_list()
  [[1, 2, 3], [5, 6]]
  """
with ops.name_scope(name, 'RaggedMask', [data, mask]):
    # Convert inputs to tensors.
    data = ragged_tensor.convert_to_tensor_or_ragged_tensor(data, name='data')
    mask = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        mask, dtypes.bool, name='mask')
    row_splits_dtype, (data, mask) = ragged_tensor.match_row_splits_dtypes(
        data, mask, return_dtype=True)

    # Get static rank of mask.
    if mask.shape.ndims is None:
        raise ValueError('mask.shape.ndims must be known statically.')
    elif mask.shape.ndims == 0:
        raise ValueError('mask cannot be scalar.')

    # If mask is ragged, then recurse with a non-ragged mask.
    if ragged_tensor.is_ragged(mask):
        if not ragged_tensor.is_ragged(data):
            data = ragged_tensor.RaggedTensor.from_tensor(
                data,
                ragged_rank=mask.ragged_rank,
                row_splits_dtype=mask.row_splits.dtype)
        # Check that mask.nested_row_splits is a prefix of
        # data.nested_row_splits.
        splits_list = [
            mask.nested_row_splits, data.nested_row_splits[:mask.ragged_rank]
        ]
        with ops.control_dependencies(
            ragged_util.assert_splits_match(splits_list)):
            # Strip off ragged `splits` until `mask` is non-ragged.  Keep the splits
            # that we strip off in `splits`, so we can add them back on after
            # we recursively mask the non-ragged data.
            splits = []
            while ragged_tensor.is_ragged(mask):
                if mask.shape.ndims > 2:
                    splits.append(mask.row_splits)
                else:
                    # Count the number of True mask values in each row to find the
                    # lengths of the filtered rows; then convert to splits.
                    int_mask = ragged_functional_ops.map_flat_values(
                        math_ops.cast, mask, dtype=row_splits_dtype)
                    masked_row_lengths = ragged_math_ops.reduce_sum(int_mask, axis=1)
                    splits.append(ragged_util.lengths_to_splits(masked_row_lengths))
                mask = mask.values
                data = data.values

            # Recursively apply the nested non-ragged mask to the nested data.
            masked_values = boolean_mask(data, mask)

            # Add the ragged `splits` back to the result.
            masked_values = ragged_tensor.RaggedTensor.from_nested_row_splits(
                masked_values, splits, validate=False)

            exit(masked_values)

    # If mask is non-ragged and has rank 1, and data is ragged, then build a
    # ragged tensor with the indicated rows.
    elif ragged_tensor.is_ragged(data) and mask.shape.ndims == 1:
        # Get the masked splits: first get the length of each row, then filter
        # out the rows that we are deleting, and convert that filtered set of
        # masks back to a splits tensor.
        lengths = data.row_lengths()
        masked_lengths = array_ops.boolean_mask(lengths, mask)
        masked_splits = ragged_util.lengths_to_splits(masked_lengths)

        # Get the masked values: first get row ids corresponding to each
        # value, then use tf.gather to build a boolean mask that's false for
        # values that come from rows that we are deleting, and use that mask to
        # construct the masked values tensor.
        segment_ids = segment_id_ops.row_splits_to_segment_ids(data.row_splits)
        segment_mask = array_ops.gather(mask, segment_ids)
        masked_values = boolean_mask(data.values, segment_mask)

        exit(ragged_tensor.RaggedTensor.from_row_splits(
            masked_values, masked_splits, validate=False))

    # If mask is non-ragged and has rank>1, then convert it to be ragged,
    # with a ragged rank matching data.
    if ragged_tensor.is_ragged(data):
        mask = ragged_tensor.RaggedTensor.from_tensor(
            mask,
            ragged_rank=min(data.ragged_rank, mask.shape.ndims - 1),
            row_splits_dtype=data.row_splits.dtype)
        exit(boolean_mask(data, mask))

    # Otherwise, data and mask are both `Tensor`s.
    else:
        # Apply `boolean_mask` to get the masked values.
        masked_values = array_ops.boolean_mask(data, mask)

        if mask.shape.ndims >= 2:
            # Add the innermost ragged dimension.  For each innermost cell, get the
            # number of values it contains.  Then flatten that to get a list of
            # cell lengths, and convert it to splits.  Finally, combine the splits
            # and values to get the innermost ragged tensor.
            masked_lengths = math_ops.count_nonzero(
                mask, axis=-1, dtype=row_splits_dtype)
            flattened_masked_lengths = array_ops.reshape(masked_lengths, [-1])
            masked_values = ragged_tensor.RaggedTensor.from_row_lengths(
                masked_values, flattened_masked_lengths, validate=False)

            # Wrap remaining ragged dimensions.
            if mask.shape.ndims > 2:
                mask_shape = array_ops.shape(mask, out_type=row_splits_dtype)
                split_size = math_ops.cumprod(mask_shape) + 1
                for dim in range(mask.shape.ndims - 3, -1, -1):
                    elt_size = mask_shape[dim + 1]
                    masked_splits = math_ops.range(split_size[dim]) * elt_size
                    masked_values = ragged_tensor.RaggedTensor.from_row_splits(
                        masked_values, masked_splits, validate=False)

        exit(masked_values)
