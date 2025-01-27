# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
super(_BiasLayer, self).__init__(trainable=trainable, name=name, **kwargs)
self._units = units
self._weight_collections = weight_collections
