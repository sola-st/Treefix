# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""A `CategoricalColumn` with a vocabulary file.

  Use this when your inputs are in string or integer format, and you have a
  vocabulary file that maps each value to an integer ID. By default,
  out-of-vocabulary values are ignored. Use either (but not both) of
  `num_oov_buckets` and `default_value` to specify how to include
  out-of-vocabulary values.

  For input dictionary `features`, `features[key]` is either `Tensor` or
  `SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
  and `''` for string, which will be dropped by this feature column.

  Example with `num_oov_buckets`:
  File `'/us/states.txt'` contains 50 lines, each with a 2-character U.S. state
  abbreviation. All inputs with values in that file are assigned an ID 0-49,
  corresponding to its line number. All other values are hashed and assigned an
  ID 50-54.

  ```python
  states = categorical_column_with_vocabulary_file(
      key='states', vocabulary_file='/us/states.txt', vocabulary_size=50,
      num_oov_buckets=5)
  columns = [states, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)
  ```

  Example with `default_value`:
  File `'/us/states.txt'` contains 51 lines - the first line is `'XX'`, and the
  other 50 each have a 2-character U.S. state abbreviation. Both a literal
  `'XX'` in input, and other values missing from the file, will be assigned
  ID 0. All others are assigned the corresponding line number 1-50.

  ```python
  states = categorical_column_with_vocabulary_file(
      key='states', vocabulary_file='/us/states.txt', vocabulary_size=51,
      default_value=0)
  columns = [states, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction, _, _ = linear_model(features, columns)
  ```

  And to make an embedding with either:

  ```python
  columns = [embedding_column(states, 3),...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  dense_tensor = input_layer(features, columns)
  ```

  Args:
    key: A unique string identifying the input feature. It is used as the column
      name and the dictionary key for feature parsing configs, feature `Tensor`
      objects, and feature columns.
    vocabulary_file: The vocabulary file name.
    vocabulary_size: Number of the elements in the vocabulary. This must be no
      greater than length of `vocabulary_file`, if less than length, later
      values are ignored. If None, it is set to the length of `vocabulary_file`.
    dtype: The type of features. Only string and integer types are supported.
    default_value: The integer ID value to return for out-of-vocabulary feature
      values, defaults to `-1`. This can not be specified with a positive
      `num_oov_buckets`.
    num_oov_buckets: Non-negative integer, the number of out-of-vocabulary
      buckets. All out-of-vocabulary inputs will be assigned IDs in the range
      `[vocabulary_size, vocabulary_size+num_oov_buckets)` based on a hash of
      the input value. A positive `num_oov_buckets` can not be specified with
      `default_value`.
    file_format: The format of the vocabulary file. The format is 'text' by
      default unless `vocabulary_file` is a string which ends in 'tfrecord.gz'.
      Accepted alternative value for `file_format` is 'tfrecord_gzip'.

  Returns:
    A `CategoricalColumn` with a vocabulary file.

  Raises:
    ValueError: `vocabulary_file` is missing or cannot be opened.
    ValueError: `vocabulary_size` is missing or < 1.
    ValueError: `num_oov_buckets` is a negative integer.
    ValueError: `num_oov_buckets` and `default_value` are both specified.
    ValueError: `dtype` is neither string nor integer.
  """
if not vocabulary_file:
    raise ValueError('Missing vocabulary_file in {}.'.format(key))

if file_format is None and vocabulary_file.endswith('tfrecord.gz'):
    file_format = 'tfrecord_gzip'

if vocabulary_size is None:
    if not gfile.Exists(vocabulary_file):
        raise ValueError('vocabulary_file in {} does not exist.'.format(key))

    if file_format == 'tfrecord_gzip':
        ds = readers.TFRecordDataset(vocabulary_file, 'GZIP')
        vocabulary_size = ds.reduce(0, lambda x, _: x + 1)
        if context.executing_eagerly():
            vocabulary_size = vocabulary_size.numpy()
    else:
        with gfile.GFile(vocabulary_file, mode='rb') as f:
            vocabulary_size = sum(1 for _ in f)
    logging.info(
        'vocabulary_size = %d in %s is inferred from the number of elements '
        'in the vocabulary_file %s.', vocabulary_size, key, vocabulary_file)

# `vocabulary_size` isn't required for lookup, but it is for `_num_buckets`.
if not isinstance(vocabulary_size, ops.Tensor) and vocabulary_size < 1:
    raise ValueError('Invalid vocabulary_size in {}.'.format(key))
if num_oov_buckets:
    if default_value is not None:
        raise ValueError(
            'Can\'t specify both num_oov_buckets and default_value in {}.'.format(
                key))
    if num_oov_buckets < 0:
        raise ValueError('Invalid num_oov_buckets {} in {}.'.format(
            num_oov_buckets, key))
fc_utils.assert_string_or_int(dtype, prefix='column_name: {}'.format(key))
fc_utils.assert_key_is_string(key)
exit(VocabularyFileCategoricalColumn(
    key=key,
    vocabulary_file=vocabulary_file,
    vocabulary_size=vocabulary_size,
    num_oov_buckets=0 if num_oov_buckets is None else num_oov_buckets,
    default_value=-1 if default_value is None else default_value,
    dtype=dtype,
    file_format=file_format))
