# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_v2_toggles.py
"""Use control flow v2.

  control flow v2 (cfv2) is an improved version of control flow in TensorFlow
  with support for higher order derivatives. Enabling cfv2 will change the
  graph/function representation of control flow, e.g., `tf.while_loop` and
  `tf.cond` will generate functional `While` and `If` ops instead of low-level
  `Switch`, `Merge` etc. ops. Note: Importing and running graphs exported
  with old control flow will still be supported.

  Calling tf.enable_control_flow_v2() lets you opt-in to this TensorFlow 2.0
  feature.

  Note: v2 control flow is always enabled inside of tf.function. Calling this
  function is not required.
  """
# pylint: disable=protected-access
logging.vlog(1, "Enabling control flow v2")
ops._control_flow_api_gauge.get_cell().set(True)
control_flow_util.ENABLE_CONTROL_FLOW_V2 = True
