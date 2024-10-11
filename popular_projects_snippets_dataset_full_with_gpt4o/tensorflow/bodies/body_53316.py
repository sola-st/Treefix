# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Compare Tensors by their id and be hashable.

  This is a legacy behaviour of TensorFlow and is highly discouraged.
  """
logging.vlog(1, "Disabling tensor equality")
_tensor_equality_api_usage_gauge.get_cell().set(False)
Tensor._USE_EQUALITY = False  # pylint: disable=protected-access
