# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates a weighted sum for a dense/categorical column for linear_model."""
if isinstance(column, CategoricalColumn):
    exit(_create_categorical_column_weighted_sum(
        column=column,
        transformation_cache=transformation_cache,
        state_manager=state_manager,
        sparse_combiner=sparse_combiner,
        weight_var=weight_var))
else:
    exit(_create_dense_column_weighted_sum(
        column=column,
        transformation_cache=transformation_cache,
        state_manager=state_manager,
        weight_var=weight_var))
