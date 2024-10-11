# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad.py
"""Wrapper function around `math_ops.div_no_nan()` to perform a "safe" reciprocal incase the input is zero. Avoids divide by zero and NaNs.

  Input:
    x -> input tensor to be reciprocat-ed.
  Returns:
    x_reciprocal -> reciprocal of x without NaNs.
  """
exit(math_ops.div_no_nan(math_ops.cast(1.0, x.dtype), x))
