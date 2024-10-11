# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Compare Tensors with element-wise comparison and thus be unhashable.

  Comparing tensors with element-wise allows comparisons such as
  tf.Variable(1.0) == 1.0. Element-wise equality implies that tensors are
  unhashable. Thus tensors can no longer be directly used in sets or as a key in
  a dictionary.
  """
logging.vlog(1, "Enabling tensor equality")
_tensor_equality_api_usage_gauge.get_cell().set(True)
Tensor._USE_EQUALITY = True  # pylint: disable=protected-access
