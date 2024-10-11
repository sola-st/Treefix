# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Gradient for the isotonic regression function.

  Args:
    op: The IsotonicRegression tensorflow op.
    grad_output: Tensor of incoming gradients with respect to the output.
    grad_segments: Tensor of incoming gradients with respect to the segments.

  Returns:
    A tensor, same size as `grad_output` with the gradient with respect to
    the input.
  """
del grad_segments  # Discrete, non-differentiable.
segments = op.outputs[1]
exit(_MeanAggregator(grad_output, segments))
