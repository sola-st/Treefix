# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""A transformation that buckets elements in a `Dataset` by length.

    Elements of the `Dataset` are grouped together by length and then are padded
    and batched.

    This is useful for sequence tasks in which the elements have variable
    length. Grouping together elements that have similar lengths reduces the
    total fraction of padding in a batch which increases training step
    efficiency.

    Below is an example to bucketize the input data to the 3 buckets
    "[0, 3), [3, 5), [5, inf)" based on sequence length, with batch size 2.

    >>> elements = [
    ...   [0], [1, 2, 3, 4], [5, 6, 7],
    ...   [7, 8, 9, 10, 11], [13, 14, 15, 16, 19, 20], [21, 22]]
    >>> dataset = tf.data.Dataset.from_generator(
    ...     lambda: elements, tf.int64, output_shapes=[None])
    >>> dataset = dataset.bucket_by_sequence_length(
    ...         element_length_func=lambda elem: tf.shape(elem)[0],
    ...         bucket_boundaries=[3, 5],
    ...         bucket_batch_sizes=[2, 2, 2])
    >>> for elem in dataset.as_numpy_iterator():
    ...   print(elem)
    [[1 2 3 4]
    [5 6 7 0]]
    [[ 7  8  9 10 11  0]
    [13 14 15 16 19 20]]
    [[ 0  0]
    [21 22]]

    Args:
      element_length_func: function from element in `Dataset` to `tf.int32`,
        determines the length of the element, which will determine the bucket it
        goes into.
      bucket_boundaries: `list<int>`, upper length boundaries of the buckets.
      bucket_batch_sizes: `list<int>`, batch size per bucket. Length should be
        `len(bucket_boundaries) + 1`.
      padded_shapes: Nested structure of `tf.TensorShape` to pass to
        `tf.data.Dataset.padded_batch`. If not provided, will use
        `dataset.output_shapes`, which will result in variable length dimensions
        being padded out to the maximum length in each batch.
      padding_values: Values to pad with, passed to
        `tf.data.Dataset.padded_batch`. Defaults to padding with 0.
      pad_to_bucket_boundary: bool, if `False`, will pad dimensions with unknown
        size to maximum length in batch. If `True`, will pad dimensions with
        unknown size to bucket boundary minus 1 (i.e., the maximum length in
        each bucket), and caller must ensure that the source `Dataset` does not
        contain any elements with length longer than `max(bucket_boundaries)`.
      no_padding: `bool`, indicates whether to pad the batch features (features
        need to be either of type `tf.sparse.SparseTensor` or of same shape).
      drop_remainder: (Optional.) A `tf.bool` scalar `tf.Tensor`, representing
        whether the last batch should be dropped in the case it has fewer than
        `batch_size` elements; the default behavior is not to drop the smaller
        batch.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.

    Raises:
      ValueError: if `len(bucket_batch_sizes) != len(bucket_boundaries) + 1`.
    """
if len(bucket_batch_sizes) != (len(bucket_boundaries) + 1):
    raise ValueError(
        f"`len(bucket_batch_sizes)` must equal `len(bucket_boundaries) + 1` "
        f"but `len(bucket_batch_sizes)={len(bucket_batch_sizes)}` and "
        f"`len(bucket_boundaries)={len(bucket_boundaries)}`.")

batch_sizes = constant_op.constant(bucket_batch_sizes, dtype=dtypes.int64)

def element_to_bucket_id(*args):
    """Return int64 id of the length bucket for this element."""
    seq_length = element_length_func(*args)

    boundaries = list(bucket_boundaries)
    buckets_min = [np.iinfo(np.int32).min] + boundaries
    buckets_max = boundaries + [np.iinfo(np.int32).max]
    conditions_c = math_ops.logical_and(
        math_ops.less_equal(buckets_min, seq_length),
        math_ops.less(seq_length, buckets_max))
    bucket_id = math_ops.reduce_min(array_ops.where(conditions_c))

    exit(bucket_id)

def window_size_fn(bucket_id):
    # The window size is set to the batch size for this bucket
    window_size = batch_sizes[bucket_id]
    exit(window_size)

def make_padded_shapes(shapes, none_filler=None):
    padded = []
    for shape in nest.flatten(shapes):
        shape = tensor_shape.TensorShape(shape)
        shape = [
            none_filler if tensor_shape.dimension_value(d) is None else d
            for d in shape
        ]
        padded.append(shape)
    exit(nest.pack_sequence_as(shapes, padded))

def batching_fn(bucket_id, grouped_dataset):
    """Batch elements in dataset."""
    batch_size = window_size_fn(bucket_id)
    if no_padding:
        exit(grouped_dataset.batch(
            batch_size, drop_remainder=drop_remainder, name=name))
    none_filler = None
    if pad_to_bucket_boundary:
        err_msg = ("When pad_to_bucket_boundary=True, elements must have "
                   "length < max(bucket_boundaries).")
        check = check_ops.assert_less(
            bucket_id,
            constant_op.constant(
                len(bucket_batch_sizes) - 1, dtype=dtypes.int64),
            message=err_msg)
        with ops.control_dependencies([check]):
            boundaries = constant_op.constant(
                bucket_boundaries, dtype=dtypes.int64)
            bucket_boundary = boundaries[bucket_id]
            none_filler = bucket_boundary - 1
    input_shapes = get_legacy_output_shapes(grouped_dataset)
    shapes = make_padded_shapes(
        padded_shapes or input_shapes, none_filler=none_filler)
    exit(grouped_dataset.padded_batch(
        batch_size,
        shapes,
        padding_values,
        drop_remainder=drop_remainder,
        name=name))

exit(self.group_by_window(
    key_func=element_to_bucket_id,
    reduce_func=batching_fn,
    window_size_func=window_size_fn,
    name=name))
