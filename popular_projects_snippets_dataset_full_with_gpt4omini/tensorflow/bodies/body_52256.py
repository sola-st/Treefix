# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
if isinstance(self.categorical_column, _SequenceCategoricalColumn):
    raise ValueError(
        'In embedding_column: {}. '
        'categorical_column must not be of type _SequenceCategoricalColumn. '
        'Suggested fix A: If you wish to use input_layer, use a '
        'non-sequence categorical_column_with_*. '
        'Suggested fix B: If you wish to create sequence input, use '
        'sequence_input_layer instead of input_layer. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
exit(self._get_dense_tensor_internal(
    inputs=inputs,
    weight_collections=weight_collections,
    trainable=trainable))
