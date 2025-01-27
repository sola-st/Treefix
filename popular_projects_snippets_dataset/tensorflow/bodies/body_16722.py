# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Creates a new VariableScope with the given properties."""
self._name = name
self._initializer = initializer
self._regularizer = regularizer
self._reuse = reuse
self._caching_device = caching_device
self._partitioner = partitioner
self._custom_getter = custom_getter
self._name_scope = name_scope
self._dtype = dtype
self._use_resource = use_resource
self._constraint = constraint
if context.executing_eagerly():
    if self._caching_device is not None:
        raise NotImplementedError("Caching devices is not yet supported "
                                  "when eager execution is enabled.")
    self._reuse = AUTO_REUSE
    self._use_resource = True
