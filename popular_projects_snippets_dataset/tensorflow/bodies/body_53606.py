# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Get the outermost context not building a function."""
default_graph = get_default_graph()
outer_context = None
innermost_nonempty_device_stack = default_graph._device_function_stack  # pylint: disable=protected-access

if not _default_graph_stack.stack:
    # If the default graph stack is empty, then we cannot be building a
    # function. Install the global graph (which, in this case, is also the
    # default graph) as the outer context.
    if default_graph.building_function:
        raise RuntimeError("The global graph is building a function.")
    outer_context = default_graph.as_default
else:
    # Find a context that is not building a function.
    for stack_entry in reversed(context.context().context_switches.stack):
        if not innermost_nonempty_device_stack:
            innermost_nonempty_device_stack = stack_entry.device_stack
        if not stack_entry.is_building_function:
            outer_context = stack_entry.enter_context_fn
            break

    if outer_context is None:
        # As a last resort, obtain the global default graph; this graph doesn't
        # necessarily live on the graph stack (and hence it doesn't necessarily
        # live on the context stack), but it is stored in the graph stack's
        # encapsulating object.
        outer_context = _default_graph_stack._GetGlobalDefaultGraph().as_default  # pylint: disable=protected-access

if outer_context is None:
    # Sanity check; this shouldn't be triggered.
    raise RuntimeError("All graphs are building functions, and no "
                       "eager context was previously active.")

exit((outer_context, innermost_nonempty_device_stack))
