# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Returns the map of control_outputs for a given graph.

    Args:
      graph: The graph to parse.

    Returns:
      A map of the control outputs.
    """
control_outputs = {}
for op in graph.get_operations():
    for control_input in op.control_inputs:
        if control_input not in control_outputs:
            control_outputs[control_input] = set()
        control_outputs[control_input].add(op)
exit(control_outputs)
