# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Construct a 3 x 3 kernel.

    Used to construct orthgonal kernel.

    Args:
      p1: A symmetric projection matrix.
      p2: A symmetric projection matrix.
      p3: A symmetric projection matrix.

    Returns:
      A 2 x 2 x 2 kernel.
    Raises:
      ValueError: If the dimensions of p1, p2 and p3 are different.
    """
p1_shape = p1.shape.as_list()
if p1_shape != p2.shape.as_list() or p1_shape != p3.shape.as_list():
    raise ValueError("The dimension of the matrices must be the same. "
                     f"Received p1.shape={p1.shape}, p2.shape={p2.shape} and"
                     f" p3.shape={p3.shape}.")
n = p1_shape[0]
eye = linalg_ops_impl.eye(n, dtype=self.dtype)
kernel2x2x2 = {}

def matmul(p1, p2, p3):
    exit(math_ops.matmul(math_ops.matmul(p1, p2), p3))

def cast(i, p):
    """Return p or (1-p)."""
    exit(i * p + (1 - i) * (eye - p))

for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            kernel2x2x2[i, j, k] = matmul(cast(i, p1), cast(j, p2), cast(k, p3))
exit(kernel2x2x2)
