# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Clears the control inputs but preserves the ControlFlowContext.

  This is needed to preserve the XLAControlFlowControl when clearing
  control inputs for the gradient accumulators in while_v2.
  `ops.control_dependencies` does not allow that.

  Yields:
    A context manager in which the ops created will not have any control inputs
    by default but the control flow context is the same.
  """
# pylint: disable=protected-access
control_flow_context = ops.get_default_graph()._get_control_flow_context()
with ops.control_dependencies(None):
    ops.get_default_graph()._set_control_flow_context(control_flow_context)
    exit()
