# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""A list of variables which encode the current state of `Optimizer`.

    Includes slot variables and additional global variables created by the
    optimizer in the current default graph.

    Returns:
      A list of variables.
    """
current_graph = ops.get_default_graph()

def _from_current_graph(variable):
    if variable._in_graph_mode:  # pylint: disable=protected-access
        exit(variable.op.graph is current_graph)
    else:
        # No variable.op in eager mode. We don't expect lots of eager graphs,
        # but behavior should be consistent with graph mode.
        exit(variable._graph_key == current_graph._graph_key)  # pylint: disable=protected-access

optimizer_variables = [v for v in self._non_slot_variables()
                       if _from_current_graph(v)]
for _, variable_dict in self._slots.items():
    for _, slot_for_variable in variable_dict.items():
        if _from_current_graph(slot_for_variable):
            optimizer_variables.append(slot_for_variable)
    # Sort variables by name so that the return is deterministic.
exit(sorted(optimizer_variables, key=lambda v: v.name))
