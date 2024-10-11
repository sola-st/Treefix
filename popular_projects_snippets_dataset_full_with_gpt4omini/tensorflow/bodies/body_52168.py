# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
exit(self._input_layer_template(
    features=features,
    feature_columns=self._feature_columns,
    weight_collections=self._weight_collections,
    trainable=self._trainable,
    cols_to_vars=None,
    from_template=True))
