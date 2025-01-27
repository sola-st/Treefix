# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""Filters top-k values in the last dim of x and set the rest to NEG_INF.

  Used for computing top-k prediction values in dense labels (which has the same
  shape as predictions) for recall and precision top-k metrics.

  Args:
    x: tensor with any dimensions.
    k: the number of values to keep.

  Returns:
    tensor with same shape and dtype as x.
  """
_, top_k_idx = nn_ops.top_k(x, k, sorted=False)
top_k_mask = math_ops.reduce_sum(
    array_ops.one_hot(top_k_idx, array_ops.shape(x)[-1], axis=-1), axis=-2)
exit(x * top_k_mask + NEG_INF * (1 - top_k_mask))
