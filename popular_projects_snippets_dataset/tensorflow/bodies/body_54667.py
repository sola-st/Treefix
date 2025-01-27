# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Creates the conversion data for the given function.

    Args:
      func: ConcreteFunction.
      lower_control_flow: Boolean indicating whether or not to lower control
        flow ops such as If and While.
      aggressive_inlining: Boolean indicating whether or not to do aggressive
        function inlining (might be unsafe if function has stateful ops, not
        properly connected to control outputs).
      variable_names_allowlist: The set of variable names to convert (by
        default, all variables are converted).
      variable_names_denylist: The set of variable names to omit converting to
        constants.
    """

self._func = func
# Inline the graph in order to remove functions when possible.
graph_def = _run_inline_graph_optimization(func, lower_control_flow,
                                           aggressive_inlining)
super(_FunctionConverterData, self).__init__(
    graph_def,
    variable_names_allowlist=variable_names_allowlist,
    variable_names_denylist=variable_names_denylist)

self._build_tensor_data()
