# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""TPU version of `tf.compat.v1.feature_column.shared_embedding_columns`.

  Note that the interface for `tf.tpu.experimental.shared_embedding_columns` is
  different from that of `tf.compat.v1.feature_column.shared_embedding_columns`:
  The following arguments are NOT supported: `ckpt_to_load_from`,
  `tensor_name_in_ckpt`, `max_norm` and `trainable`.

  Use this function in place of
  tf.compat.v1.feature_column.shared_embedding_columns` when you want to use the
  TPU to accelerate your embedding lookups via TPU embeddings.

  ```
  column_a = tf.feature_column.categorical_column_with_identity(...)
  column_b = tf.feature_column.categorical_column_with_identity(...)
  tpu_columns = tf.tpu.experimental.shared_embedding_columns(
      [column_a, column_b], 10)
  ...
  def model_fn(features):
    dense_feature = tf.keras.layers.DenseFeature(tpu_columns)
    embedded_feature = dense_feature(features)
    ...

  estimator = tf.estimator.tpu.TPUEstimator(
      model_fn=model_fn,
      ...
      embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
          column=tpu_columns,
          ...))
  ```

  Args:
    categorical_columns: A list of categorical columns returned from
      `categorical_column_with_identity`, `weighted_categorical_column`,
      `categorical_column_with_vocabulary_file`,
      `categorical_column_with_vocabulary_list`,
      `sequence_categorical_column_with_identity`,
      `sequence_categorical_column_with_vocabulary_file`,
      `sequence_categorical_column_with_vocabulary_list`
    dimension: An integer specifying dimension of the embedding, must be > 0.
    combiner: A string specifying how to reduce if there are multiple entries in
      a single row for a non-sequence column. For more information, see
      `tf.feature_column.embedding_column`.
    initializer: A variable initializer function to be used in embedding
      variable initialization. If not specified, defaults to
      `tf.truncated_normal_initializer` with mean `0.0` and standard deviation
      `1/sqrt(dimension)`.
    shared_embedding_collection_name: Optional name of the collection where
      shared embedding weights are added. If not given, a reasonable name will
      be chosen based on the names of `categorical_columns`. This is also used
      in `variable_scope` when creating shared embedding weights.
    max_sequence_lengths: An list of non-negative integers, either None or empty
      or the same length as the argument categorical_columns. Entries
      corresponding to non-sequence columns must be 0 and entries corresponding
      to sequence columns specify the max sequence length for the column. Any
      sequence shorter then this will be padded with 0 embeddings and any
      sequence longer will be truncated.
    learning_rate_fn: A function that takes global step and returns learning
      rate for the embedding table. If you intend to use the same learning rate
      for multiple embedding tables, please ensure that you pass the exact same
      python function to all calls of shared_embedding_columns, otherwise
      performence may suffer.
    embedding_lookup_device: The device on which to run the embedding lookup.
      Valid options are "cpu", "tpu_tensor_core", and "tpu_embedding_core". If
      specifying "tpu_tensor_core", a tensor_core_shape must be supplied.
      Defaults to "cpu". If not specified, the default behavior is embedding
      lookup on "tpu_embedding_core" for training and "cpu" for inference.
      Valid options for training : ["tpu_embedding_core", "tpu_tensor_core"]
      Valid options for serving :  ["cpu", "tpu_tensor_core"]
      For training, tpu_embedding_core is good for large embedding vocab (>1M),
      otherwise, tpu_tensor_core is often sufficient.
      For serving, doing embedding lookup on tpu_tensor_core during serving is
      a way to reduce host cpu usage in cases where that is a bottleneck.
    tensor_core_shape: If supplied, a list of integers which specifies the
      intended dense shape to run embedding lookup for this feature on
      TensorCore. The batch dimension can be left None or -1 to indicate a
      dynamic shape. Only rank 2 shapes currently supported.
    use_safe_embedding_lookup: If true, uses safe_embedding_lookup_sparse
      instead of embedding_lookup_sparse. safe_embedding_lookup_sparse ensures
      there are no empty rows and all weights and ids are positive at the
      expense of extra compute cost. This only applies to rank 2 (NxM) shaped
      input tensors. Defaults to true, consider turning off if the above checks
      are not needed. Note that having empty rows will not trigger any error
      though the output result might be 0 or omitted.

  Returns:
    A  list of `_TPUSharedEmbeddingColumnV2`.

  Raises:
    ValueError: if `dimension` not > 0.
    ValueError: if `initializer` is specified but not callable.
    ValueError: if `max_sequence_lengths` is specified and not the same length
      as `categorical_columns`.
    ValueError: if `max_sequence_lengths` is positive for a non sequence column
      or 0 for a sequence column.
  """

for categorical_column in categorical_columns:
    if not isinstance(categorical_column, _SUPPORTED_CATEGORICAL_COLUMNS_V2):
        raise TypeError(
            'categorical_column for tpu '
            ' shared_embedding_columns must be type {}, got {}.'.format(
                ' or '.join(
                    [cc.__name__ for cc in _SUPPORTED_CATEGORICAL_COLUMNS_V2]),
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
if tensor_core_shape and len(tensor_core_shape) != 2:
    raise ValueError(
        'tensor_core_shape must be size 2. Got {}.'.format(tensor_core_shape))

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

column_creator = fc_lib.SharedEmbeddingColumnCreator(
    dimension=dimension, initializer=initializer, ckpt_to_load_from=None,
    tensor_name_in_ckpt=None, num_buckets=num_buckets, trainable=None,
    name=shared_embedding_collection_name)

if (embedding_lookup_device and
    embedding_lookup_device not in _ALLOWED_DEVICES):
    raise ValueError(
        f'If set, embedding_lookup_device must be in {_ALLOWED_DEVICES}')

if embedding_lookup_device == 'cpu':
    embedding_lookup_device = EmbeddingDevice.CPU
elif embedding_lookup_device == 'tpu_tensor_core':
    embedding_lookup_device = EmbeddingDevice.TPU_TENSOR_CORE
elif embedding_lookup_device == 'tpu_embedding_core':
    embedding_lookup_device = EmbeddingDevice.TPU_EMBEDDING_CORE

if embedding_lookup_device == EmbeddingDevice.TPU_TENSOR_CORE:
    if not tensor_core_shape:
        raise ValueError('Using embedding_lookup_device=tpu_tensor_core requires '
                         'tensor_core_shape to be set.')
    for c in sorted_columns:
        if isinstance(c, _SUPPORTED_SEQUENCE_COLUMNS):
            raise ValueError('embedding_lookup_device=tpu_tensor_core currently '
                             'does not support sequence columns.')

  # Create the state (_SharedEmbeddingColumnLayer) here.
for categorical_column, max_sequence_length in zip(
    categorical_columns, max_sequence_lengths):
    if not embedding_lookup_device:
        column = _TPUSharedEmbeddingColumnV2(
            categorical_column=categorical_column,
            shared_embedding_column_creator=column_creator,
            combiner=combiner,
            initializer=initializer,
            shared_embedding_collection_name=shared_embedding_collection_name,
            max_sequence_length=max_sequence_length,
            learning_rate_fn=learning_rate_fn,
            use_safe_embedding_lookup=use_safe_embedding_lookup)
    else:
        column = _TPUSharedDeviceSpecificEmbeddingColumnV2(
            categorical_column=categorical_column,
            shared_embedding_column_creator=column_creator,
            combiner=combiner,
            initializer=initializer,
            shared_embedding_collection_name=shared_embedding_collection_name,
            max_sequence_length=max_sequence_length,
            learning_rate_fn=learning_rate_fn,
            embedding_lookup_device=embedding_lookup_device,
            tensor_core_shape=tensor_core_shape,
            use_safe_embedding_lookup=use_safe_embedding_lookup)
    tpu_columns.append(column)

exit(tpu_columns)
