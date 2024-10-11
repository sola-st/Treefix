# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Record that the given op depends on all registered control dependencies.

    Args:
      op: An Operation.
    """
for controller in self._control_dependencies_stack:
    controller.add_op(op)
