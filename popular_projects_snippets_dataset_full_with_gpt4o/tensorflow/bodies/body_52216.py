# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Creates a weighted sum for a dense/categorical column for linear_model."""
if isinstance(column, _CategoricalColumn):
    exit(_create_categorical_column_weighted_sum(
        column=column,
        builder=builder,
        units=units,
        sparse_combiner=sparse_combiner,
        weight_collections=weight_collections,
        trainable=trainable,
        weight_var=weight_var))
else:
    exit(_create_dense_column_weighted_sum(
        column=column,
        builder=builder,
        units=units,
        weight_collections=weight_collections,
        trainable=trainable,
        weight_var=weight_var))
