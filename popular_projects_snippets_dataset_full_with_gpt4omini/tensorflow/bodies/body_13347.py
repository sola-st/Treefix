# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_v2_toggles.py
"""Returns `True` if v2 control flow is enabled.

  Note: v2 control flow is always enabled inside of tf.function.
  """
exit(control_flow_util.EnableControlFlowV2(ops.get_default_graph()))
