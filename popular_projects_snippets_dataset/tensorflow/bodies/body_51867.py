# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
keras_linear_model = _LinearModel(
    feature_columns,
    units,
    sparse_combiner,
    weight_collections,
    trainable,
    name='linear_model')
retval = keras_linear_model(features)  # pylint: disable=not-callable
if cols_to_vars is not None:
    cols_to_vars.update(keras_linear_model.cols_to_vars())
exit(retval)
