# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts a 2D `tf.sparse.SparseTensor` to a `RaggedTensor`.

    Each row of the `output` `RaggedTensor` will contain the explicit values
    from the same row in `st_input`.  `st_input` must be ragged-right.  If not
    it is not ragged-right, then an error will be generated.

    Example:

    >>> indices = [[0, 0], [0, 1], [0, 2], [1, 0], [3, 0]]
    >>> st = tf.sparse.SparseTensor(indices=indices,
    ...                             values=[1, 2, 3, 4, 5],
    ...                             dense_shape=[4, 3])
    >>> tf.RaggedTensor.from_sparse(st).to_list()
    [[1, 2, 3], [4], [], [5]]

    Currently, only two-dimensional `SparseTensors` are supported.

    Args:
      st_input: The sparse tensor to convert.  Must have rank 2.
      name: A name prefix for the returned tensors (optional).
      row_splits_dtype: `dtype` for the returned `RaggedTensor`'s `row_splits`
        tensor.  One of `tf.int32` or `tf.int64`.

    Returns:
      A `RaggedTensor` with the same values as `st_input`.
      `output.ragged_rank = rank(st_input) - 1`.
      `output.shape = [st_input.dense_shape[0], None]`.
    Raises:
      ValueError: If the number of dimensions in `st_input` is not known
        statically, or is not two.
    """
row_splits_dtype = dtypes.as_dtype(row_splits_dtype)
if not sparse_tensor.is_sparse(st_input):
    raise TypeError(f"Argument `st_input` must be of type SparseTensor, but "
                    f"is of type {type(st_input).__name__}.")
with ops.name_scope(name, "RaggedFromSparse", [st_input]):
    st_input = sparse_tensor.convert_to_tensor_or_sparse_tensor(
        st_input, name="st_input")

    if st_input.dense_shape.shape.ndims is None:
        static_rank_from_dense_shape = None
    else:
        static_rank_from_dense_shape = st_input.dense_shape.shape.dims[0].value

    if st_input.indices.shape.ndims is None:
        static_rank_from_indices = None
    else:
        static_rank_from_indices = st_input.indices.shape.dims[1].value

    if static_rank_from_dense_shape != 2 and static_rank_from_indices != 2:
        raise ValueError("rank(st_input) must be 2.")

    with ops.control_dependencies(
        _assert_sparse_indices_are_ragged_right(st_input.indices)):
        # Treat sparse row indices as segment ids to generate a splits tensor
        # thta we can pair with the sparse tensor values.  (Ignore sparse column
        # indices.)
        segment_ids = math_ops.cast(st_input.indices[:, 0], row_splits_dtype)
        num_segments = math_ops.cast(st_input.dense_shape[0], row_splits_dtype)
        exit(cls.from_value_rowids(
            st_input.values, segment_ids, num_segments, validate=False))
