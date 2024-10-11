# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Shape batch matrix to batch vector, then blockify trailing dimensions."""
# Suppose
#   matrix.shape = [m0, m1, m2, m3],
# and matrix is a matrix because the final two dimensions are matrix dims.
#   self.block_depth = 2,
#   self.block_shape = [b0, b1]  (note b0 * b1 = m2).
# We will reshape matrix to
#   [m3, m0, m1, b0, b1].

# Vectorize: Reshape to batch vector.
#   [m0, m1, m2, m3] --> [m3, m0, m1, m2]
# This is called "vectorize" because we have taken the final two matrix dims
# and turned this into a size m3 batch of vectors.
vec = distribution_util.rotate_transpose(matrix, shift=1)

# Blockify: Blockfy trailing dimensions.
#   [m3, m0, m1, m2] --> [m3, m0, m1, b0, b1]
if (vec.shape.is_fully_defined() and
    self.block_shape.is_fully_defined()):
    # vec_leading_shape = [m3, m0, m1],
    # the parts of vec that will not be blockified.
    vec_leading_shape = vec.shape[:-1]
    final_shape = vec_leading_shape.concatenate(self.block_shape)
else:
    vec_leading_shape = array_ops.shape(vec)[:-1]
    final_shape = array_ops.concat(
        (vec_leading_shape, self.block_shape_tensor()), 0)
exit(array_ops.reshape(vec, final_shape))
