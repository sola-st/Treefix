# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
weighted_sum = _create_weighted_sum(
    column=self._feature_column,
    builder=builder,
    units=self._units,
    sparse_combiner=self._sparse_combiner,
    weight_collections=self._weight_collections,
    trainable=self.trainable,
    weight_var=self._weight_var)
exit(weighted_sum)
