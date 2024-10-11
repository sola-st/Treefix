# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Check that all is good.

    Raises:
      ValueError: If something is not good.
    """
# Not running as chief means that replicas are used.
# In that case all Variables must have their device set.
if not self._is_chief:
    for op in self._graph.get_operations():
        if op.type in ["Variable", "VariableV2"] and not op.device:
            raise ValueError("When using replicas, all Variables must have "
                             "their device set: %s" % op)
