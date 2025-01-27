# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Represents discretized dense input.

  Buckets include the left boundary, and exclude the right boundary. Namely,
  `boundaries=[0., 1., 2.]` generates buckets `(-inf, 0.)`, `[0., 1.)`,
  `[1., 2.)`, and `[2., +inf)`.

  For example, if the inputs are

  ```python
  boundaries = [0, 10, 100]
  input tensor = [[-5, 10000]
                  [150,   10]
                  [5,    100]]
  ```

  then the output will be

  ```python
  output = [[0, 3]
            [3, 2]
            [1, 3]]
  ```

  Example:

  ```python
  price = numeric_column('price')
  bucketized_price = bucketized_column(price, boundaries=[...])
  columns = [bucketized_price, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)

  # or
  columns = [bucketized_price, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  dense_tensor = input_layer(features, columns)
  ```

  A `bucketized_column` can also be crossed with another categorical column
  using `crossed_column`:

  ```python
  price = numeric_column('price')
  # bucketized_column converts numerical feature to a categorical one.
  bucketized_price = bucketized_column(price, boundaries=[...])
  # 'keywords' is a string feature.
  price_x_keywords = crossed_column([bucketized_price, 'keywords'], 50K)
  columns = [price_x_keywords, ...]
  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  linear_prediction = linear_model(features, columns)
  ```

  Args:
    source_column: A one-dimensional dense column which is generated with
      `numeric_column`.
    boundaries: A sorted list or tuple of floats specifying the boundaries.

  Returns:
    A `_BucketizedColumn`.

  Raises:
    ValueError: If `source_column` is not a numeric column, or if it is not
      one-dimensional.
    ValueError: If `boundaries` is not a sorted list or tuple.
  """
if not isinstance(source_column, _NumericColumn):
    raise ValueError(
        'source_column must be a column generated with numeric_column(). '
        'Given: {}'.format(source_column))
if len(source_column.shape) > 1:
    raise ValueError('source_column must be one-dimensional column. '
                     'Given: {}'.format(source_column))
if (not boundaries or
    not (isinstance(boundaries, list) or isinstance(boundaries, tuple))):
    raise ValueError('boundaries must be a sorted list.')
for i in range(len(boundaries) - 1):
    if boundaries[i] >= boundaries[i + 1]:
        raise ValueError('boundaries must be a sorted list.')
exit(_BucketizedColumn(source_column, tuple(boundaries)))
