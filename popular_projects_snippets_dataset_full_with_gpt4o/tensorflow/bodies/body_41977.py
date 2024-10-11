# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Returns a `ConcreteFunction` specialized to inputs and execution context.

    Unlike `get_concrete_function(...)`, the graph will be deleted when the
    returned function is deleted.  It's useful to avoid creating a reference
    cycle when you know for sure that the graph will be no longer used without
    the returned function.

    Args:
      *args: inputs to specialize on.
      **kwargs: inputs to specialize on.
    """
if self.input_signature:
    self._function_spec.validate_inputs_with_signature(args, kwargs)

with self._lock:
    concrete_function, _ = self._maybe_define_concrete_function(args, kwargs)
    seen_names = set()
    concrete_function._arg_keywords = []  # pylint: disable=protected-access
    prefix_counts = {}
    graph = concrete_function.graph
    num_captures = len(
        graph.internal_captures + graph.deferred_internal_captures)
    num_positional = len(graph.inputs) - num_captures
    for arg in concrete_function.graph.inputs[:num_positional]:
        user_arg_name = compat.as_str(arg.op.get_attr("_user_specified_name"))
        proposal = user_arg_name
        while proposal in seen_names:
            index = prefix_counts.get(user_arg_name, 1)
            proposal = "{}_{}".format(user_arg_name, index)
            prefix_counts[user_arg_name] = index + 1
        seen_names.add(proposal)
        concrete_function._arg_keywords.append(proposal)  # pylint: disable=protected-access
    # Anything can be a positional argument, in the same order as .inputs
    concrete_function._num_positional_args = num_positional  # pylint: disable=protected-access
    exit(concrete_function)
