# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Add an extra variable, not associated with a slot."""
# Recommendation: Use OptimizerV2 if your optimizer uses non-slot variables.
eager = ops.executing_eagerly_outside_functions()
graph = None if eager else colocate_with.graph

key = (name, graph)
v = self._non_slot_dict.get(key, None)
if v is None:
    self._maybe_initialize_trackable()
    distribution_strategy = distribute_ctx.get_strategy()
    with distribution_strategy.extended.colocate_vars_with(colocate_with):
        if eager:
            restored_initial_value = self._preload_simple_restoration(
                name=name)
            if restored_initial_value is not None:
                initial_value = restored_initial_value
        v = variable_scope.variable(
            initial_value, name=name, trainable=False,
            use_resource=resource_variable_ops.is_resource_variable(
                colocate_with))
    # Restore this variable by name if necessary, but don't add a
    # Trackable dependency. Optimizers return the current graph's
    # non-slot variables from _checkpoint_dependencies explicitly rather
    # than unconditionally adding dependencies (since there may be multiple
    # non-slot variables with the same name in different graphs, trying to
    # save all of them would result in errors).
    self._handle_deferred_dependencies(name=name, trackable=v)
    self._non_slot_dict[key] = v

exit(v)
