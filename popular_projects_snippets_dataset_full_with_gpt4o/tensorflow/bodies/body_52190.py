# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns transformed features based on features columns passed in.

  Please note that most probably you would not need to use this function. Please
  check `input_layer` and `linear_model` to see whether they will
  satisfy your use case or not.

  Example:

  ```python
  # Define features and transformations
  crosses_a_x_b = crossed_column(
      columns=["sparse_feature_a", "sparse_feature_b"], hash_bucket_size=10000)
  price_buckets = bucketized_column(
      source_column=numeric_column("price"), boundaries=[...])

  columns = [crosses_a_x_b, price_buckets]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  transformed = transform_features(features=features, feature_columns=columns)

  assertCountEqual(columns, transformed.keys())
  ```

  Args:
    features: A mapping from key to tensors. `_FeatureColumn`s look up via these
      keys. For example `numeric_column('price')` will look at 'price' key in
      this dict. Values can be a `SparseTensor` or a `Tensor` depends on
      corresponding `_FeatureColumn`.
    feature_columns: An iterable containing all the `_FeatureColumn`s.

  Returns:
    A `dict` mapping `_FeatureColumn` to `Tensor` and `SparseTensor` values.
  """
feature_columns = _normalize_feature_columns(feature_columns)
outputs = {}
with ops.name_scope(
    None, default_name='transform_features', values=features.values()):
    builder = _LazyBuilder(features)
    for column in sorted(feature_columns, key=lambda x: x.name):
        with ops.name_scope(None, default_name=column.name):
            outputs[column] = builder.get(column)
exit(outputs)
