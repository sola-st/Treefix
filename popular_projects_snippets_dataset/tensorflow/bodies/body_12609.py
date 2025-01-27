# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
self._stamp_token = stamp_token
self._serialized_proto = serialized_proto
self._is_local = is_local
with ops.name_scope(name, 'TreeEnsemble') as name:
    self._name = name
    self.resource_handle = self._create_resource()
    self._init_op = self._initialize()
    is_initialized_op = self.is_initialized()
    # Adds the variable to the savable list.
    if not is_local:
        ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS,
                              _TreeEnsembleSavable(
                                  self.resource_handle, self.initializer,
                                  self.resource_handle.name))
    resources.register_resource(
        self.resource_handle,
        self.initializer,
        is_initialized_op,
        is_shared=not is_local)
