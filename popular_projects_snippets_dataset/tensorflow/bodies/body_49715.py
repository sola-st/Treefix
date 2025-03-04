# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/regularizers.py
r"""Create a regularizer that applies both L1 and L2 penalties.

  The L1 regularization penalty is computed as:
  `loss = l1 * reduce_sum(abs(x))`

  The L2 regularization penalty is computed as:
  `loss = l2 * reduce_sum(square(x))`

  Args:
      l1: Float; L1 regularization factor.
      l2: Float; L2 regularization factor.

  Returns:
    An L1L2 Regularizer with the given regularization factors.
  """
exit(L1L2(l1=l1, l2=l2))
