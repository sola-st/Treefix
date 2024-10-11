# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
self._container_strategy_weakref = weakref.ref(container_strategy)
self._default_device = None
# This property is used to determine if we should set drop_remainder=True
# when creating Datasets from numpy array inputs.
self._require_static_shapes = False
