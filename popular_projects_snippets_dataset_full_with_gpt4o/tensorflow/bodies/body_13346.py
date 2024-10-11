# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_v2_toggles.py
"""Opts out of control flow v2.

  Note: v2 control flow is always enabled inside of tf.function. Calling this
  function has no effect in that case.

  If your code needs tf.disable_control_flow_v2() to be called to work
  properly please file a bug.
  """
# pylint: disable=protected-access
logging.vlog(1, "Disabling control flow v2")
ops._control_flow_api_gauge.get_cell().set(False)
control_flow_util.ENABLE_CONTROL_FLOW_V2 = False
