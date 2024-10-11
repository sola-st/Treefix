# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""The derivative provided by CTC Loss.

  Args:
     op: the CTCLoss op.
     grad_loss: The backprop for cost.

  Returns:
     The CTC Loss gradient.
  """
exit(_CTCLossGradImpl(op, grad_loss, _))
