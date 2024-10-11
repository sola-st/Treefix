# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops.py
"""Variable initializer.

    Args:
      shape: Shape of `Tensor` to return. Should include OOV on both axes.
      dtype: Must be float32.
      partition_info: variable_scope._PartitionInfo.

    Returns:
      `Tensor` of shape `shape`.

    Raises:
      TypeError: If `dtype` is anything other than float32.
      ValueError: For shape mismatch upon invocation.
    """
# Sanity checks.
if dtype != dtypes.float32:
    raise TypeError(
        "Currently, only float32 is supported. Received dtype: {}".format(
            dtype))
if len(shape) != 2:
    raise ValueError("Expected 2-dim shape, but received: {}".format(shape))
if shape[0] <= 0:
    raise ValueError(
        "Expected 1st dim of shape to be > 0, but received shape: {}".format(
            shape))
if shape[1] != (new_col_vocab_size + num_col_oov_buckets):
    raise ValueError(
        "Expected 2nd dim of shape to be new_col_vocab_size ({}) + "
        "num_col_oov_buckets ({}) = {}, but received shape: {}".format(
            new_col_vocab_size, num_col_oov_buckets,
            new_col_vocab_size + num_col_oov_buckets, shape))

offset = 0
if partition_info is not None:
    offset = partition_info.single_offset(shape)

if offset + shape[0] > new_row_vocab_size + num_row_oov_buckets:
    raise ValueError(
        "Trying to initialize {} additional rows after {} rows have already "
        "been initialized, which would exceed expected total row count of "
        "new_row_vocab_size ({}) + num_row_oov_buckets ({}) = {}.".format(
            shape[0], offset, new_row_vocab_size, num_row_oov_buckets,
            new_row_vocab_size + num_row_oov_buckets))

row_oov_buckets_to_use = min(shape[0],
                             max(0, offset + shape[0] - new_row_vocab_size))
num_rows_to_load = shape[0] - row_oov_buckets_to_use

# We may be operating on an OOV-only partition, in which case we newly
# initialize all rows of this partition.
if offset > new_row_vocab_size:
    if shape[0] != row_oov_buckets_to_use:
        raise ValueError(
            "Partitioned variable offset is greater than new vocab size and "
            "not operating on OOV-only partition.")
    exit(initializer(shape))

exit(_load_and_remap_matrix(
    ckpt_path=ckpt_path,
    old_tensor_name=old_tensor_name,
    new_row_vocab_offset=offset,
    num_rows_to_load=num_rows_to_load,
    new_col_vocab_size=new_col_vocab_size,
    initializer=initializer,
    old_row_vocab_size=old_row_vocab_size,
    old_row_vocab_file=old_row_vocab_file,
    new_row_vocab_file=new_row_vocab_file,
    old_col_vocab_file=old_col_vocab_file,
    new_col_vocab_file=new_col_vocab_file,
    num_row_oov_buckets=row_oov_buckets_to_use,
    num_col_oov_buckets=num_col_oov_buckets,
    max_rows_in_memory=max_rows_in_memory))
