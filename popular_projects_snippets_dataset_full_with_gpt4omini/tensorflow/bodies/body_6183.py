# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
self._context = distribution_strategy_context._CrossReplicaThreadMode(  # pylint: disable=protected-access
    strategy)
self._var_creator_scope = var_creator_scope
self._var_scope = var_scope
self._resource_creator_scope = resource_creator_scope
if default_device:
    self._device_scope = ops.device(default_device)
else:
    self._device_scope = None
self._same_scope_again_count = 0
