# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Construct a 2 x 2 kernel.

    Used to construct orthgonal kernel.

    Args:
      p1: A symmetric projection matrix.
      p2: A symmetric projection matrix.

    Returns:
      A 2 x 2 kernel [[p1p2,         p1(1-p2)],
                      [(1-p1)p2, (1-p1)(1-p2)]].
    Raises:
      ValueError: If the dimensions of p1 and p2 are different.
    """
if p1.shape.as_list() != p2.shape.as_list():
    raise ValueError("The dimension of the matrices must be the same. "
                     f"Received p1.shape={p1.shape} and p2.shape={p2.shape}.")
n = p1.shape.as_list()[0]
kernel2x2 = {}
eye = linalg_ops_impl.eye(n, dtype=self.dtype)
kernel2x2[0, 0] = math_ops.matmul(p1, p2)
kernel2x2[0, 1] = math_ops.matmul(p1, (eye - p2))
kernel2x2[1, 0] = math_ops.matmul((eye - p1), p2)
kernel2x2[1, 1] = math_ops.matmul((eye - p1), (eye - p2))

exit(kernel2x2)
