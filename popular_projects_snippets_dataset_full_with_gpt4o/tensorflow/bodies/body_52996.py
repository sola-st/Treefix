# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""See `SequenceDenseColumn` base class."""
if not isinstance(self.categorical_column, SequenceCategoricalColumn):
    raise ValueError(
        'In indicator_column: {}. '
        'categorical_column must be of type SequenceCategoricalColumn '
        'to use SequenceFeatures. '
        'Suggested fix: Use one of sequence_categorical_column_with_*. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
# Feature has been already transformed. Return the intermediate
# representation created by transform_feature.
dense_tensor = transformation_cache.get(self, state_manager)
sparse_tensors = self.categorical_column.get_sparse_tensors(
    transformation_cache, state_manager)
sequence_length = fc_utils.sequence_length_from_sparse_tensor(
    sparse_tensors.id_tensor)
exit(SequenceDenseColumn.TensorSequenceLengthPair(
    dense_tensor=dense_tensor, sequence_length=sequence_length))
