# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""The derivative provided by CTC Loss V2.

  Args:
     op: the CTCLossV2 op.
     grad_loss: The backprop for cost.

  Returns:
     The CTC Loss V2 gradient.
  """
exit(_CTCLossGradImpl(op, grad_loss, _))
