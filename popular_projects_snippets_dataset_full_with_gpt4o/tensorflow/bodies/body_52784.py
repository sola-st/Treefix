# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Represents real valued or numerical features.

  Example:

  Assume we have data with two features `a` and `b`.

  >>> data = {'a': [15, 9, 17, 19, 21, 18, 25, 30],
  ...    'b': [5.0, 6.4, 10.5, 13.6, 15.7, 19.9, 20.3 , 0.0]}

  Let us represent the features `a` and `b` as numerical features.

  >>> a = tf.feature_column.numeric_column('a')
  >>> b = tf.feature_column.numeric_column('b')

  Feature column describe a set of transformations to the inputs.

  For example, to "bucketize" feature `a`, wrap the `a` column in a
  `feature_column.bucketized_column`.
  Providing `5` bucket boundaries, the bucketized_column api
  will bucket this feature in total of `6` buckets.

  >>> a_buckets = tf.feature_column.bucketized_column(a,
  ...    boundaries=[10, 15, 20, 25, 30])

  Create a `DenseFeatures` layer which will apply the transformations
  described by the set of `tf.feature_column` objects:

  >>> feature_layer = tf.keras.layers.DenseFeatures([a_buckets, b])
  >>> print(feature_layer(data))
  tf.Tensor(
  [[ 0.   0.   1.   0.   0.   0.   5. ]
   [ 1.   0.   0.   0.   0.   0.   6.4]
   [ 0.   0.   1.   0.   0.   0.  10.5]
   [ 0.   0.   1.   0.   0.   0.  13.6]
   [ 0.   0.   0.   1.   0.   0.  15.7]
   [ 0.   0.   1.   0.   0.   0.  19.9]
   [ 0.   0.   0.   0.   1.   0.  20.3]
   [ 0.   0.   0.   0.   0.   1.   0. ]], shape=(8, 7), dtype=float32)

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    shape: An iterable of integers specifies the shape of the `Tensor`. An
      integer can be given which means a single dimension `Tensor` with given
      width. The `Tensor` representing the column will have the shape of
      [batch_size] + `shape`.
    default_value: A single value compatible with `dtype` or an iterable of
      values compatible with `dtype` which the column takes on during
      `tf.Example` parsing if data is missing. A default value of `None` will
      cause `tf.io.parse_example` to fail if an example does not contain this
      column. If a single value is provided, the same value will be applied as
      the default value for every item. If an iterable of values is provided,
      the shape of the `default_value` should be equal to the given `shape`.
    dtype: defines the type of values. Default value is `tf.float32`. Must be a
      non-quantized, real integer or floating point type.
    normalizer_fn: If not `None`, a function that can be used to normalize the
      value of the tensor after `default_value` is applied for parsing.
      Normalizer function takes the input `Tensor` as its argument, and returns
      the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
      even though the most common use case of this function is normalization, it
      can be used for any kind of Tensorflow transformations.

  Returns:
    A `NumericColumn`.

  Raises:
    TypeError: if any dimension in shape is not an int
    ValueError: if any dimension in shape is not a positive integer
    TypeError: if `default_value` is an iterable but not compatible with `shape`
    TypeError: if `default_value` is not compatible with `dtype`.
    ValueError: if `dtype` is not convertible to `tf.float32`.
  """
shape = _check_shape(shape, key)
if not (dtype.is_integer or dtype.is_floating):
    raise ValueError('dtype must be convertible to float. '
                     'dtype: {}, key: {}'.format(dtype, key))
default_value = fc_utils.check_default_value(shape, default_value, dtype, key)

if normalizer_fn is not None and not callable(normalizer_fn):
    raise TypeError(
        'normalizer_fn must be a callable. Given: {}'.format(normalizer_fn))

fc_utils.assert_key_is_string(key)
exit(NumericColumn(
    key,
    shape=shape,
    default_value=default_value,
    dtype=dtype,
    normalizer_fn=normalizer_fn))
