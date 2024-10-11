# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/inplace_ops.py
"""Applies an inplace add on input x at index i with value v. Aliases x.

  If i is None, x and v must be the same shape. Computes
    x += v;
  If i is a scalar, x has a rank 1 higher than v's. Computes
    x[i, :] += v;
  Otherwise, x and v must have the same rank. Computes
    x[i, :] += v;

  Args:
    x: A Tensor.
    i: None, a scalar or a vector.
    v: A Tensor.

  Returns:
    Returns x.

  """
exit(_inplace_helper(x, i, v, gen_array_ops.inplace_add))
