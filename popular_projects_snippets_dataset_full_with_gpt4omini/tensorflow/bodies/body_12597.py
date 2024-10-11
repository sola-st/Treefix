# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
del max_elements  # Unused.

self._eps = epsilon
self._num_streams = num_streams
self._num_quantiles = num_quantiles

with ops.name_scope(name, 'QuantileAccumulator') as name:
    self._name = name
    self.resource_handle = self._create_resource()
    self._init_op = self._initialize()
    is_initialized_op = self.is_initialized()
resources.register_resource(self.resource_handle, self._init_op,
                            is_initialized_op)
ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS,
                      QuantileAccumulatorSaveable(
                          self.resource_handle, self._init_op,
                          self._num_streams, self.resource_handle.name))
