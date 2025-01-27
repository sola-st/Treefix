# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
super(_FCLinearWrapper, self).__init__(
    trainable=trainable, name=name, **kwargs)
self._feature_column = feature_column
self._units = units
self._sparse_combiner = sparse_combiner
self._weight_collections = weight_collections
