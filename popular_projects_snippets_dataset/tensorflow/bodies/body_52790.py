# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""A `CategoricalColumn` that returns identity values.

  Use this when your inputs are integers in the range `[0, num_buckets)`, and
  you want to use the input value itself as the categorical ID. Values outside
  this range will result in `default_value` if specified, otherwise it will
  fail.

  Typically, this is used for contiguous ranges of integer indexes, but
  it doesn't have to be. This might be inefficient, however, if many of IDs
  are unused. Consider `categorical_column_with_hash_bucket` in that case.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  In the following examples, each input in the range `[0, 1000000)` is assigned
  the same value. All other inputs are assigned `default_value` 0. Note that a
  literal 0 in inputs will result in the same default ID.

  Linear model:

  ```python
  import tensorflow as tf
  video_id = tf.feature_column.categorical_column_with_identity(
      key='video_id', num_buckets=1000000, default_value=0)
  columns = [video_id]
  features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],
  [33,78, 2, 73, 1]])}
  linear_prediction = tf.compat.v1.feature_column.linear_model(features,
  columns)
  ```

  Embedding for a DNN model:

  ```python
  import tensorflow as tf
  video_id = tf.feature_column.categorical_column_with_identity(
      key='video_id', num_buckets=1000000, default_value=0)
  columns = [tf.feature_column.embedding_column(video_id, 9)]
  features = {'video_id': tf.sparse.from_dense([[2, 85, 0, 0, 0],
  [33,78, 2, 73, 1]])}
  input_layer = tf.keras.layers.DenseFeatures(columns)
  dense_tensor = input_layer(features)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    num_buckets: Range of inputs and outputs is `[0, num_buckets)`.
    default_value: If set, values outside of range `[0, num_buckets)` will be
      replaced with this value. If not set, values >= num_buckets will cause a
      failure while values < 0 will be dropped.

  Returns:
    A `CategoricalColumn` that returns identity values.

  Raises:
    ValueError: if `num_buckets` is less than one.
    ValueError: if `default_value` is not in range `[0, num_buckets)`.
  """
if num_buckets < 1:
    raise ValueError('num_buckets {} < 1, column_name {}'.format(
        num_buckets, key))
if (default_value is not None) and ((default_value < 0) or
                                    (default_value >= num_buckets)):
    raise ValueError(
        'default_value {} not in range [0, {}), column_name {}'.format(
            default_value, num_buckets, key))
fc_utils.assert_key_is_string(key)
exit(IdentityCategoricalColumn(
    key=key, number_buckets=num_buckets, default_value=default_value))
