# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Return the gradients for L2Loss.

  Args:
    op: The L2LossOp for which we need to generate gradients.
    grad: Tensor containing a single number.

  Returns:
    The gradient, which is (x * grad).
  """
exit(op.inputs[0] * grad)
