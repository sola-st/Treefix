# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
self._tpu_categorical_column = categorical_column
self._max_sequence_length = max_sequence_length
self._learning_rate_fn = learning_rate_fn
if (self.is_sequence_column() and max_sequence_length < 1):
    raise ValueError('max_sequence_length must be greater than 0 for '
                     'sequence columns. Got max_sequence_length={} for '
                     'sequence column {}.'.format(max_sequence_length,
                                                  categorical_column.name))
if (not self.is_sequence_column() and max_sequence_length != 0):
    raise ValueError('Non zero max_seq_length={} specified for non '
                     'sequence column {}.'.format(max_sequence_length,
                                                  categorical_column.name))
