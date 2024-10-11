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
      session: Session object.
    """
self._session = session

session.run(variables.global_variables_initializer())
# Run extra assignment ops if needed.
# These assignments are run sequentially to ensure order.
for op in ops.get_default_graph().get_collection(VAR_ASSIGN_COLLECTION):
    session.run(op)

super(_FunctionConverterDataInGraph, self).__init__(
    func,
    lower_control_flow,
    aggressive_inlining,
    variable_names_allowlist,
    variable_names_denylist)
