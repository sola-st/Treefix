# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Creates parsing spec dictionary from input feature_columns.

  The returned dictionary can be used as arg 'features' in
  `tf.io.parse_example`.

  Typical usage example:

  ```python
  # Define features and transformations
  feature_a = categorical_column_with_vocabulary_file(...)
  feature_b = numeric_column(...)
  feature_c_bucketized = bucketized_column(numeric_column("feature_c"), ...)
  feature_a_x_feature_c = crossed_column(
      columns=["feature_a", feature_c_bucketized], ...)

  feature_columns = set(
      [feature_b, feature_c_bucketized, feature_a_x_feature_c])
  features = tf.io.parse_example(
      serialized=serialized_examples,
      features=make_parse_example_spec(feature_columns))
  ```

  For the above example, make_parse_example_spec would return the dict:

  ```python
  {
      "feature_a": parsing_ops.VarLenFeature(tf.string),
      "feature_b": parsing_ops.FixedLenFeature([1], dtype=tf.float32),
      "feature_c": parsing_ops.FixedLenFeature([1], dtype=tf.float32)
  }
  ```

  Args:
    feature_columns: An iterable containing all feature columns. All items
      should be instances of classes derived from `_FeatureColumn`.

  Returns:
    A dict mapping each feature key to a `FixedLenFeature` or `VarLenFeature`
    value.

  Raises:
    ValueError: If any of the given `feature_columns` is not a `_FeatureColumn`
      instance.
  """
result = {}
for column in feature_columns:
    if not isinstance(column, _FeatureColumn):
        raise ValueError('All feature_columns must be _FeatureColumn instances. '
                         'Given: {}'.format(column))
    config = column._parse_example_spec  # pylint: disable=protected-access
    for key, value in six.iteritems(config):
        if key in result and value != result[key]:
            raise ValueError('feature_columns contain different parse_spec for key '
                             '{}. Given {} and {}'.format(key, value, result[key]))
    result.update(config)
exit(result)
