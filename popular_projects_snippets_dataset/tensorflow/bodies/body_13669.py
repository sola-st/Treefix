# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
"""Calculate the batched KL divergence KL(n_a || n_b) with n_a and n_b Normal.

  Args:
    n_a: instance of a Normal distribution object.
    n_b: instance of a Normal distribution object.
    name: (optional) Name to use for created operations.
      default is "kl_normal_normal".

  Returns:
    Batchwise KL(n_a || n_b)
  """
with ops.name_scope(name, "kl_normal_normal", [n_a.loc, n_b.loc]):
    one = constant_op.constant(1, dtype=n_a.dtype)
    two = constant_op.constant(2, dtype=n_a.dtype)
    half = constant_op.constant(0.5, dtype=n_a.dtype)
    s_a_squared = math_ops.square(n_a.scale)
    s_b_squared = math_ops.square(n_b.scale)
    ratio = s_a_squared / s_b_squared
    exit((math_ops.squared_difference(n_a.loc, n_b.loc) / (two * s_b_squared)
            + half * (ratio - one - math_ops.log(ratio))))
