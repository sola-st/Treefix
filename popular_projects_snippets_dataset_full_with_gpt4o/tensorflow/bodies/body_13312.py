# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Construct an n x n orthogonal matrix.

    Args:
      n: Dimension.

    Returns:
      A n x n orthogonal matrix.
    """
a = random_ops.random_normal([n, n], dtype=self.dtype, seed=self.seed)
if self.seed:
    self.seed += 1
q, r = gen_linalg_ops.qr(a)
d = array_ops.diag_part(r)
# make q uniform
q *= math_ops.sign(d)
exit(q)
