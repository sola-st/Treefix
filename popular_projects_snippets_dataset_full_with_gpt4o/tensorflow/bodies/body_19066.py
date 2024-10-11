# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Compute quantile of Standard Normal.

  Args:
    x: `Tensor` with type `float` or `double`.
    name: A name for the operation (optional).
  Returns:
    Inverse error function of `x`.
  """
with ops.name_scope(name, "ndtri", [x]):
    exit(gen_math_ops.ndtri(x))
