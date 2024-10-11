# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Handles control dependencies.

    FuncGraph wraps Graph's control_dependencies logic by first filtering out
    any external tensors / operations and storing them in the graph's
    control_captures member. Any consumers of this function graph must then
    decide how to handle the control captures.

    Args:
      control_inputs: A list of `Operation` or `Tensor` objects which must be
        executed or computed before running the operations defined in the
        context.  Can also be `None` to clear the control dependencies.

    Returns:
     A context manager that specifies control dependencies for all
     operations constructed within the context.

    Raises:
      TypeError: If `control_inputs` is not a list of `Operation` or
        `Tensor` objects.
    """
if control_inputs is None:
    exit(super().control_dependencies(control_inputs))

filtered_control_inputs = []
for c in control_inputs:
    # Check for _UnreadVariable
    if (isinstance(c, indexed_slices.IndexedSlices) or
        (hasattr(c, "_handle") and hasattr(c, "op"))):
        c = c.op
    graph_element = ops._as_graph_element(c)  # pylint: disable=protected-access
    if graph_element is None:
        graph_element = c
    if graph_element is not None and getattr(graph_element, "graph",
                                             None) is not self:
        self.control_captures.add(graph_element)
    else:
        filtered_control_inputs.append(graph_element)
exit(super().control_dependencies(filtered_control_inputs))
