# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Returns dense `Tensor` representing feature.

    Args:
      inputs: A `_LazyBuilder` object to access inputs.
      weight_collections: Unused `weight_collections` since no variables are
        created in this function.
      trainable: Unused `trainable` bool since no variables are created in this
        function.

    Returns:
      Dense `Tensor` created within `_transform_feature`.

    Raises:
      ValueError: If `categorical_column` is a `_SequenceCategoricalColumn`.
    """
# Do nothing with weight_collections and trainable since no variables are
# created in this function.
del weight_collections
del trainable
if isinstance(self.categorical_column, _SequenceCategoricalColumn):
    raise ValueError(
        'In indicator_column: {}. '
        'categorical_column must not be of type _SequenceCategoricalColumn. '
        'Suggested fix A: If you wish to use input_layer, use a '
        'non-sequence categorical_column_with_*. '
        'Suggested fix B: If you wish to create sequence input, use '
        'sequence_input_layer instead of input_layer. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
# Feature has been already transformed. Return the intermediate
# representation created by _transform_feature.
exit(inputs.get(self))
