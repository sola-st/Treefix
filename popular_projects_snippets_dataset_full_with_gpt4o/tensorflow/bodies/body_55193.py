# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Context manager for copying distribute.Strategy scope information."""
# pylint: disable=protected-access
# TODO(b/112906995, nareshmodi): distribution strategy depends on
# inheriting this stack from the default graph even in eager mode. Maybe
# it should be part of the eager context? This would also allow us to
# remove a get_default_graph() call from the function cache lookup.
graph = ops.get_default_graph()
old_strategy_stack = self._distribution_strategy_stack
self._distribution_strategy_stack = list(
    graph._distribution_strategy_stack)

# We ignore device placements from any outer scopes while tracing the
# function when possible, to avoid hard-coding them in the function
# graph. "Default" placements come from the PartitionedCallOp's placement,
# so that the same trace of the Python function may be placed on several
# different devices and saved functions may be placed on new devices when
# restored.
# However, we need to preserve the outer device stack in the following
# cases in non eager context:
# 1. device stack is callable
# 2. When using distribution strategy with legacy graph mode.
old_device_stack = self._device_function_stack
if (not context.executing_eagerly() and
    (device_stack_has_callable(graph._device_function_stack) or
     (self._distribution_strategy_stack and
      not ops.executing_eagerly_outside_functions()))):
    # Hard-code devices from device functions in the function body
    self._device_function_stack = graph._device_function_stack.copy()

old_creator_stack = self._variable_creator_stack
self._variable_creator_stack = graph._variable_creator_stack
# Inherit the graph key, since this is used for matching variables in
# optimizers.
old_graph_key = self._graph_key
self._graph_key = graph._graph_key
# pylint: enable=protected-access

old_scope_exit_callbacks = self._scope_exit_callbacks
self._scope_exit_callbacks = []

with outer_cm as g:
    try:
        exit(g)
    finally:
        try:
            for fn in self._scope_exit_callbacks:
                fn()
        finally:
            self._scope_exit_callbacks = old_scope_exit_callbacks
            self._distribution_strategy_stack = old_strategy_stack
            self._device_function_stack = old_device_stack
            self._variable_creator_stack = old_creator_stack
            self._graph_key = old_graph_key
