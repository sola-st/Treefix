# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""Split a list of _TPUEmbeddingColumn into sequence and non-sequence columns.

  For use in a TPUEstimator model_fn function. E.g.

  def model_fn(features):
    sequence_columns, feature_columns = (
        tf.tpu.feature_column.split_sequence_columns(feature_columns))
    input = tf.feature_column.input_layer(
        features=features, feature_columns=feature_columns)
    sequence_features, sequence_lengths = (
        tf.contrib.feature_column.sequence_input_layer(
            features=features, feature_columns=sequence_columns))

  Args:
    feature_columns: A list of _TPUEmbeddingColumns to split.

  Returns:
    Two lists of _TPUEmbeddingColumns, the first is the sequence columns and the
    second is the non-sequence columns.
  """
sequence_columns = []
non_sequence_columns = []
for column in feature_columns:
    if not isinstance(column, (_TPUEmbeddingColumnV2,
                               _TPUSharedEmbeddingColumnV2)):
        raise TypeError(
            'column must be a _TPUEmbeddingColumnV2 or '
            f'_TPUSharedEmbeddingColumnV2 but got {type(column)} instead.')
    if column.is_sequence_column():
        sequence_columns.append(column)
    else:
        non_sequence_columns.append(column)
exit((sequence_columns, non_sequence_columns))
