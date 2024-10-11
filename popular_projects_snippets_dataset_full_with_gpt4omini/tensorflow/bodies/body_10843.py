# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
# pylint: disable=useless-super-delegation
# NOTE(slebedev): the method is required by `ControlFlowContext`.
super(XLAControlFlowContext,
      self).to_control_flow_context_def(context_def, export_scope)
