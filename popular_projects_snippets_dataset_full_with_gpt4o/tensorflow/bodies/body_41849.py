# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_context.py
"""Generates a FunctionContext based on current contextual info."""
ctx = context.context()

# Don't need to open an init_scope if the tf.function call is in eager mode
# already.
executing_eagerly = ctx.executing_eagerly()
parent_graph = None
xla_context_id = 0
if not executing_eagerly:
    # We want to force function retracing for each different
    # XLAControlFlowContext, so add `xla_context_id` to the context.
    xla_context = _enclosing_xla_context()
    if xla_context is not None and xla_context.RequiresUniqueFunctionRetracing(
    ):
        xla_context_id = id(xla_context)

    with ops.init_scope():
        # The graph, or whether we're executing eagerly, should be a part of the
        # cache key so we don't improperly capture tensors such as variables.
        executing_eagerly = ctx.executing_eagerly()
        parent_graph = None if executing_eagerly else ops.get_default_graph()

  # pylint: disable=protected-access
default_graph = ops.get_default_graph()
# TODO(b/117617952): The current distribution strategy will affect graph
# building (e.g. accessing different variables from different devices) and
# so requires retracing for each device.
strategy_stack = default_graph._distribution_strategy_stack
uses_distribution_strategy = (
    strategy_stack and
    strategy_stack[-1].strategy.extended._retrace_functions_for_each_device)
if executing_eagerly:
    colocation_stack = ()
    if uses_distribution_strategy:
        device_functions = (pydev.merge_device(ctx.device_name),)
    else:
        device_functions = ()
else:
    colocation_stack = tuple(default_graph._colocation_stack.peek_objs())
    if (uses_distribution_strategy or
        func_graph_module.device_stack_has_callable(
            default_graph._device_function_stack)):
        # Putting the device in the cache key ensures that call-site device
        # annotations are respected.
        device_functions = tuple(default_graph._device_functions_outer_to_inner)
    else:
        device_functions = ()

in_cross_replica_context = False
try:
    in_cross_replica_context = (strategy_stack[-1].replica_context is None)  # pylint: disable=protected-access
except (AttributeError, IndexError):
    pass

if save_context.in_save_context():
    variable_policy = (
        save_context.get_save_options().experimental_variable_policy)
else:
    variable_policy = None

exit(function_cache.FunctionContext(
    EagerContext(parent_graph, device_functions, colocation_stack,
                 in_cross_replica_context, variable_policy, xla_context_id)))
