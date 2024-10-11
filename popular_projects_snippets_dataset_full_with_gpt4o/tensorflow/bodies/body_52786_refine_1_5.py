hash_bucket_size = 10 # pragma: no cover
key = 'keywords' # pragma: no cover
dtype = str # pragma: no cover
HashedCategoricalColumn = type('HashedCategoricalColumn', (object,), {}) # pragma: no cover
fc_utils = type('Mock', (object,), {'assert_key_is_string': lambda key: None, 'assert_string_or_int': lambda dtype, prefix: None}) # pragma: no cover

hash_bucket_size = 10 # pragma: no cover
key = 'keywords' # pragma: no cover
HashedCategoricalColumn = type('HashedCategoricalColumn', (object,), {'__init__': lambda self, key, hash_bucket_size, dtype: setattr(self, 'params', (key, hash_bucket_size, dtype))}) # pragma: no cover
fc_utils = type('Mock', (object,), {'assert_key_is_string': lambda self, key: None, 'assert_string_or_int': lambda self, dtype, prefix: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
from l3.Runtime import _l_
"""Represents sparse feature where ids are set by hashing.

  Use this when your sparse features are in string or integer format, and you
  want to distribute your inputs into a finite number of buckets by hashing.
  output_id = Hash(input_feature_string) % bucket_size for string type input.
  For int type input, the value is converted to its string representation first
  and then hashed by the same formula.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  Example:

  ```python
  import tensorflow as tf
  keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
  10000)
  columns = [keywords]
  features = {'keywords': tf.constant([['Tensorflow', 'Keras', 'RNN', 'LSTM',
  'CNN'], ['LSTM', 'CNN', 'Tensorflow', 'Keras', 'RNN'], ['CNN', 'Tensorflow',
  'LSTM', 'Keras', 'RNN']])}
  linear_prediction, _, _ = tf.compat.v1.feature_column.linear_model(features,
  columns)

  # or
  import tensorflow as tf
  keywords = tf.feature_column.categorical_column_with_hash_bucket("keywords",
  10000)
  keywords_embedded = tf.feature_column.embedding_column(keywords, 16)
  columns = [keywords_embedded]
  features = {'keywords': tf.constant([['Tensorflow', 'Keras', 'RNN', 'LSTM',
  'CNN'], ['LSTM', 'CNN', 'Tensorflow', 'Keras', 'RNN'], ['CNN', 'Tensorflow',
  'LSTM', 'Keras', 'RNN']])}
  input_layer = tf.keras.layers.DenseFeatures(columns)
  dense_tensor = input_layer(features)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    hash_bucket_size: An int > 1. The number of buckets.
    dtype: The type of features. Only string and integer types are supported.

  Returns:
    A `HashedCategoricalColumn`.

  Raises:
    ValueError: `hash_bucket_size` is not greater than 1.
    ValueError: `dtype` is neither string nor integer.
  """
if hash_bucket_size is None:
    _l_(20206)

    raise ValueError('hash_bucket_size must be set. ' 'key: {}'.format(key))
    _l_(20205)

if hash_bucket_size < 1:
    _l_(20208)

    raise ValueError('hash_bucket_size must be at least 1. '
                     'hash_bucket_size: {}, key: {}'.format(
                         hash_bucket_size, key))
    _l_(20207)

fc_utils.assert_key_is_string(key)
_l_(20209)
fc_utils.assert_string_or_int(dtype, prefix='column_name: {}'.format(key))
_l_(20210)
aux = HashedCategoricalColumn(key, hash_bucket_size, dtype)
_l_(20211)

exit(aux)
