# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Opts out of resource variables.

  If your code needs tf.disable_resource_variables() to be called to work
  properly please file a bug.
  """
global _DEFAULT_USE_RESOURCE
_DEFAULT_USE_RESOURCE = False
logging.vlog(1, "Disabling resource variables")
_api_usage_gauge.get_cell().set(False)
