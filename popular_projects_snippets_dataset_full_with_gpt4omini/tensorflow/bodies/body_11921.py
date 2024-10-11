# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Flatten the block dimensions then reshape to a batch matrix."""
# Suppose
#   vec.shape = [v0, v1, v2, v3],
#   self.block_depth = 2.
# Then
#   leading shape = [v0, v1]
#   block shape = [v2, v3].
# We will reshape vec to
#   [v1, v2*v3, v0].

# Un-blockify: Flatten block dimensions.  Reshape
#   [v0, v1, v2, v3] --> [v0, v1, v2*v3].
vec_flat = self._unblockify(vec)

# Matricize:  Reshape to batch matrix.
#   [v0, v1, v2*v3] --> [v1, v2*v3, v0],
# representing a shape [v1] batch of [v2*v3, v0] matrices.
matrix = distribution_util.rotate_transpose(vec_flat, shift=-1)
exit(matrix)
