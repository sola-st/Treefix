# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Return the control outputs for a given op.

    Args:
      op: The op to fetch control outputs for.

    Returns:
      Iterable of control output ops.
    """
if op.graph not in self.cache:
    control_outputs = self.calc_control_outputs(op.graph)
    self.cache[op.graph] = control_outputs
else:
    control_outputs = self.cache[op.graph]
exit(control_outputs.get(op, []))
