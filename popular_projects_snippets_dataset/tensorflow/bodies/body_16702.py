# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Creates resource variables by default.

  Resource variables are improved versions of TensorFlow variables with a
  well-defined memory model. Accessing a resource variable reads its value, and
  all ops which access a specific read value of the variable are guaranteed to
  see the same value for that tensor. Writes which happen after a read (by
  having a control or data dependency on the read) are guaranteed not to affect
  the value of the read tensor, and similarly writes which happen before a read
  are guaranteed to affect the value. No guarantees are made about unordered
  read/write pairs.

  Calling tf.enable_resource_variables() lets you opt-in to this TensorFlow 2.0
  feature.
  """
global _DEFAULT_USE_RESOURCE
_DEFAULT_USE_RESOURCE = True
logging.vlog(1, "Enabling resource variables")
_api_usage_gauge.get_cell().set(True)
