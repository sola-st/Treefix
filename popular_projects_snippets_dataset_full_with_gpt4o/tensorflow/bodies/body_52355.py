# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column.py
"""A sequence of categorical terms where ids are set by hashing.

  Pass this to `embedding_column` or `indicator_column` to convert sequence
  categorical data into dense representation for input to sequence NN, such as
  RNN.

  Example:

  ```python
  tokens = sequence_categorical_column_with_hash_bucket(
      'tokens', hash_bucket_size=1000)
  tokens_embedding = embedding_column(tokens, dimension=10)
  columns = [tokens_embedding]

  features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
  sequence_feature_layer = SequenceFeatures(columns)
  sequence_input, sequence_length = sequence_feature_layer(features)
  sequence_length_mask = tf.sequence_mask(sequence_length)

  rnn_cell = tf.keras.layers.SimpleRNNCell(hidden_size)
  rnn_layer = tf.keras.layers.RNN(rnn_cell)
  outputs, state = rnn_layer(sequence_input, mask=sequence_length_mask)
  ```

  Args:
    key: A unique string identifying the input feature.
    hash_bucket_size: An int > 1. The number of buckets.
    dtype: The type of features. Only string and integer types are supported.

  Returns:
    A `SequenceCategoricalColumn`.

  Raises:
    ValueError: `hash_bucket_size` is not greater than 1.
    ValueError: `dtype` is neither string nor integer.
  """
exit(fc.SequenceCategoricalColumn(
    fc.categorical_column_with_hash_bucket(
        key=key, hash_bucket_size=hash_bucket_size, dtype=dtype)))
