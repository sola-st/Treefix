# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Disables the V2 TensorShape behavior and reverts to V1 behavior.

  See docstring for `enable_v2_tensorshape` for details about the new behavior.
  """
global _TENSORSHAPE_V2_OVERRIDE  # pylint: disable=invalid-name
_TENSORSHAPE_V2_OVERRIDE = False
logging.vlog(1, "Disabling v2 tensorshape")
_api_usage_gauge.get_cell().set(False)
