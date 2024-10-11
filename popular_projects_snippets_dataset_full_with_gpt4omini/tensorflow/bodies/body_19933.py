# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
"""List of dense columns that convert from sparse, categorical input.

  Note that the interface for TPU embedding_column is different from the non-TPU
  version. The following args available for the non-TPU version are NOT
  supported: ckpt_to_load_from, tensor_name_in_ckp, max_norm and trainable.

  Args:
    categorical_columns: A list of categorical_columns returned from
        categorical_column_with_identity, weighted_categorical_column,
        categorical_column_with_vocabulary_file,
        categorical_column_with_vocabulary_list,
        sequence_categorical_column_with_identity,
        sequence_categorical_column_with_vocabulary_file,
        sequence_categorical_column_with_vocabulary_list
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries
      in a single row for a non-sequence column. For more information, see
      `tf.feature_column.embedding_column`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `tf.truncated_normal_initializer` with mean `0.0` and standard deviation
      `1/sqrt(dimension)`.
    shared_embedding_collection_name: Optional name of the collection where
      shared embedding weights are added. If not given, a reasonable name will
      be chosen based on the names of `categorical_columns`. This is also used
      in `variable_scope` when creating shared embedding weights.
    max_sequence_lengths: An list of non-negative integers, either None or
      empty or the same length as the argument categorical_columns. Entries
      corresponding to non-sequence columns must be 0 and entries corresponding
      to sequence columns specify the max sequence length for the column. Any
      sequence shorter then this will be padded with 0 embeddings and any
      sequence longer will be truncated.
    learning_rate_fn: A function that takes global step and returns learning
      rate for the embedding table. If you intend to use the same learning rate
      for multiple embedding tables, please ensure that you pass the exact same
      python function to all calls of shared_embedding_columns, otherwise
      performence may suffer.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    A  _TPUEmbeddingColumn.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if `initializer` is specified but not callable.
    ValueError: if `max_sequence_lengths` is specified and not the same length
      as `categorical_columns`.
    ValueError: if `max_sequence_lengths` is positive for a non sequence column
      or 0 for a sequence column.
  """
for categorical_column in categorical_columns:
    if isinstance(categorical_column, _DENYLISTED_CATEGORICAL_COLUMNS_V2):
        raise TypeError('categorical_column for tpu '
                        ' embedding_column was denylisted type '
                        f'{type(categorical_column)}')
    if not isinstance(categorical_column, _SUPPORTED_CATEGORICAL_COLUMNS):
        raise TypeError(
            'categorical_column for tpu '
            ' shared_embedding_columns must be type {}, got {}.'.format(
                ' or '.join(
                    [cc.__name__ for cc in _SUPPORTED_CATEGORICAL_COLUMNS]),
                type(categorical_column)))

if not max_sequence_lengths:
    max_sequence_lengths = [0] * len(categorical_columns)
if len(max_sequence_lengths) != len(categorical_columns):
    raise ValueError('max_sequence_lengths and categorical_columns must be of '
                     'the same length. len(max_sequence_lengths)={} '
                     'len(categorical_columns)={}.'.format(
                         len(max_sequence_lengths), len(categorical_columns)))

if (dimension is None) or (dimension < 1):
    raise ValueError('Invalid dimension {}.'.format(dimension))

if (initializer is not None) and (not callable(initializer)):
    raise ValueError('initializer must be callable if specified. ')
if initializer is None:
    initializer = init_ops.truncated_normal_initializer(
        mean=0.0, stddev=1 / math.sqrt(dimension))

# Sort the columns so the default collection name is deterministic even if the
# user passes columns from an unsorted collection, such as dict.values().
sorted_columns = sorted(categorical_columns, key=lambda x: x.name)
num_buckets = sorted_columns[0]._num_buckets  # pylint: disable=protected-access

for c in sorted_columns[1:]:
    if num_buckets != c._num_buckets:  # pylint: disable=protected-access
        raise ValueError(
            'To use shared_embedding_column, all categorical_columns must have '
            'the same number of buckets. Given column: {} with buckets: {} does  '
            'not match column: {} with buckets: {}'.format(
                sorted_columns[0], num_buckets, c, c._num_buckets))  # pylint: disable=protected-access

if not shared_embedding_collection_name:
    shared_embedding_collection_name = '_'.join(c.name for c in sorted_columns)
    shared_embedding_collection_name += '_shared_embedding'

tpu_columns = []

# Create the state (_SharedEmbeddingColumnLayer) here.
for categorical_column, max_sequence_length in zip(
    categorical_columns, max_sequence_lengths):
    column = _TPUSharedEmbeddingColumn(
        categorical_column=categorical_column,
        dimension=dimension,
        combiner=combiner,
        initializer=initializer,
        shared_embedding_collection_name=shared_embedding_collection_name,
        ckpt_to_load_from=None,
        tensor_name_in_ckpt=None,
        max_norm=None,
        trainable=True,
        max_sequence_length=max_sequence_length,
        learning_rate_fn=learning_rate_fn,
        use_safe_embedding_lookup=use_safe_embedding_lookup)
    tpu_columns.append(column)

exit(tpu_columns)
