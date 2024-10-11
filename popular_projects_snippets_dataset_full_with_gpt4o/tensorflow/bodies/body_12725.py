# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""The gradient for log_softmax.

      log_softmax = input - log(sum(exp(input))
      dlog_softmax/dinput = diag - softmax(input)

  Args:
    op: The log softmax op.
    grad: The tensor representing the gradient w.r.t. the output.

  Returns:
    The gradients w.r.t. the input.
  """
softmax = math_ops.exp(op.outputs[0])
exit(grad - math_ops.reduce_sum(grad, -1, keepdims=True) * softmax)
