# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Allow this scope to be entered if this strategy is already in scope.
if distribution_strategy_context.has_strategy():
    _require_cross_replica_or_default_context_extended(
        self._context.strategy.extended)
    self._same_scope_again_count += 1
else:
    _push_per_thread_mode(self._context)
    if self._var_scope:
        self._var_scope.__enter__()
    self._var_creator_scope.__enter__()
    if self._resource_creator_scope:
        nest.map_structure(lambda scope: scope.__enter__(),
                           self._resource_creator_scope)
    if self._device_scope:
        self._device_scope.__enter__()
exit(self._context.strategy)
