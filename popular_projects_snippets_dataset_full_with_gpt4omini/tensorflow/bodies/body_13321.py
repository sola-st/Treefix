# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
"""Construct a kernel.

    Used to construct orthgonal kernel.

    Args:
      projection_matrix: A symmetric projection matrix of size n x n.

    Returns:
      [projection_matrix, (1 - projection_matrix)].
    """
n = projection_matrix.shape.as_list()[0]
kernel = {}
eye = linalg_ops_impl.eye(n, dtype=self.dtype)
kernel[0] = projection_matrix
kernel[1] = eye - projection_matrix
exit(kernel)
