# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
"""TPU embedding_column for `tf.feature_column.embedding_column`.

  Note that the interface for TPU embedding_column is different from the non-TPU
  version. The following args available for the non-TPU version are NOT
  supported: ckpt_to_load_from, tensor_name_in_ckp, max_norm and trainable.

  Args:
    categorical_column: A categorical_column returned from
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
      `tf.compat.v1.truncated_normal_initializer` with mean `0.0` and
      standard deviation `1/sqrt(dimension)`.
    max_sequence_length: An non-negative integer specifying the max sequence
      length. Any sequence shorter then this will be padded with 0 embeddings
      and any sequence longer will be truncated. This must be positive for
      sequence features and 0 for non-sequence features.
    learning_rate_fn: A function that takes global step and returns learning
      rate for the embedding table. If you intend to use the same learning rate
      for multiple embedding tables, please ensure that you pass the exact same
      python function to all calls of embedding_column, otherwise performence
      may suffer.
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
    TypeError: if categorical_column is not a supported type.
  """
if isinstance(categorical_column, _DENYLISTED_CATEGORICAL_COLUMNS_V2):
    raise TypeError('categorical_column for tpu '
                    ' embedding_column was '
                    f'denylisted type {type(categorical_column)}')
if not isinstance(categorical_column, _SUPPORTED_CATEGORICAL_COLUMNS):
    raise TypeError(
        'categorical_column for tpu '
        ' embedding_column must be type {}, got {}.'.format(' or '.join([
            cc.__name__ for cc in _SUPPORTED_CATEGORICAL_COLUMNS
        ]), type(categorical_column)))
if (dimension is None) or (dimension < 1):
    raise ValueError('Invalid dimension {}.'.format(dimension))

if (initializer is not None) and (not callable(initializer)):
    raise ValueError('initializer must be callable if specified. '
                     'Embedding of column_name: {}'.format(
                         categorical_column.name))
if initializer is None:
    initializer = init_ops.truncated_normal_initializer(
        mean=0.0, stddev=1 / math.sqrt(dimension))

embedding_shape = categorical_column._num_buckets, dimension  # pylint: disable=protected-access

def _creator(weight_collections, scope):
    embedding_column_layer = fc._EmbeddingColumnLayer(
        embedding_shape=embedding_shape,
        initializer=initializer,
        weight_collections=weight_collections,
        trainable=True,
        name='embedding_column_layer')
    exit(embedding_column_layer(None, scope=scope))  # pylint: disable=not-callable

column = _TPUEmbeddingColumn(
    categorical_column=categorical_column,
    dimension=dimension,
    combiner=combiner,
    layer_creator=_creator,
    ckpt_to_load_from=None,
    tensor_name_in_ckpt=None,
    max_norm=None,
    trainable=True,
    max_sequence_length=max_sequence_length,
    learning_rate_fn=learning_rate_fn,
    use_safe_embedding_lookup=use_safe_embedding_lookup)
# For Embedding column, the initializer is hidden inside the creator Fn, which
# is not accessible later. So, we attach it to a special field. Also note
# that non-TPU Embedding column and non-TPU shared Embedding column handle the
# initializer differently. See shared_embedding_columns for details.
column._tpu_initializer = initializer
exit(column)
