# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""A dataset of all files matching one or more glob patterns.

    The `file_pattern` argument should be a small number of glob patterns.
    If your filenames have already been globbed, use
    `Dataset.from_tensor_slices(filenames)` instead, as re-globbing every
    filename with `list_files` may result in poor performance with remote
    storage systems.

    Note: The default behavior of this method is to return filenames in
    a non-deterministic random shuffled order. Pass a `seed` or `shuffle=False`
    to get results in a deterministic order.

    Example:
      If we had the following files on our filesystem:

        - /path/to/dir/a.txt
        - /path/to/dir/b.py
        - /path/to/dir/c.py

      If we pass "/path/to/dir/*.py" as the directory, the dataset
      would produce:

        - /path/to/dir/b.py
        - /path/to/dir/c.py

    Args:
      file_pattern: A string, a list of strings, or a `tf.Tensor` of string type
        (scalar or vector), representing the filename glob (i.e. shell wildcard)
        pattern(s) that will be matched.
      shuffle: (Optional.) If `True`, the file names will be shuffled randomly.
        Defaults to `True`.
      seed: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the random
        seed that will be used to create the distribution. See
        `tf.random.set_seed` for behavior.
      name: Optional. A name for the tf.data operations used by `list_files`.

    Returns:
     Dataset: A `Dataset` of strings corresponding to file names.
    """
with ops.name_scope("list_files"):
    if shuffle is None:
        shuffle = True
    file_pattern = ops.convert_to_tensor(
        file_pattern, dtype=dtypes.string, name="file_pattern")
    matching_files = gen_io_ops.matching_files(file_pattern)

    # Raise an exception if `file_pattern` does not match any files.
    condition = math_ops.greater(array_ops.shape(matching_files)[0], 0,
                                 name="match_not_empty")

    message = math_ops.add(
        "No files matched pattern: ",
        string_ops.reduce_join(file_pattern, separator=", "), name="message")

    assert_not_empty = control_flow_ops.Assert(
        condition, [message], summarize=1, name="assert_not_empty")
    with ops.control_dependencies([assert_not_empty]):
        matching_files = array_ops.identity(matching_files)

    # TODO(b/240947712): Remove lazy import after this method is factored out.
    # Loaded lazily due to a circular dependency (dataset_ops ->
    # from_tensor_slices_op -> dataset_ops).
    # pylint: disable=g-import-not-at-top,protected-access
    from tensorflow.python.data.ops import from_tensor_slices_op
    dataset = from_tensor_slices_op._TensorSliceDataset(
        matching_files, is_files=True, name=name)
    # pylint: enable=g-import-not-at-top,protected-access
    if issubclass(Dataset, DatasetV1):
        dataset = DatasetV1Adapter(dataset)
    if shuffle:
        # NOTE(mrry): The shuffle buffer size must be greater than zero, but the
        # list of files might be empty.
        buffer_size = math_ops.maximum(
            array_ops.shape(matching_files, out_type=dtypes.int64)[0], 1)
        dataset = dataset.shuffle(buffer_size, seed=seed, name=name)
    exit(dataset)
