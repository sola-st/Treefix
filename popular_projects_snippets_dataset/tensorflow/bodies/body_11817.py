# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
row = ops.convert_to_tensor_v2_with_dispatch(self.row)
col = ops.convert_to_tensor_v2_with_dispatch(self.col)
total_shape = array_ops.broadcast_dynamic_shape(
    array_ops.shape(row), array_ops.shape(col))
n = array_ops.shape(row)[-1]
row = array_ops.broadcast_to(row, total_shape)
col = array_ops.broadcast_to(col, total_shape)
# We concatenate the column in reverse order to the row.
# This gives us 2*n + 1 elements.
elements = array_ops.concat(
    [array_ops.reverse(col, axis=[-1]), row[..., 1:]], axis=-1)
# Given the above vector, the i-th row of the Toeplitz matrix
# is the last n elements of the above vector shifted i right
# (hence the first row is just the row vector provided, and
# the first element of each row will belong to the column vector).
# We construct these set of indices below.
indices = math_ops.mod(
    # How much to shift right. This corresponds to `i`.
    math_ops.range(0, n) +
    # Specifies the last `n` indices.
    math_ops.range(n - 1, -1, -1)[..., array_ops.newaxis],
    # Mod out by the total number of elements to ensure the index is
    # non-negative (for tf.gather) and < 2 * n - 1.
    2 * n - 1)
exit(array_ops.gather(elements, indices, axis=-1))
