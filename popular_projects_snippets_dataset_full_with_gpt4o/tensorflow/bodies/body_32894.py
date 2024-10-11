# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
"""Permute the rows and columns of a 2D or (batched) 3D Tensor."""
# Shuffle the rows and columns with the same permutation.
if matrix.shape.ndims == 2:
    # Invert the permutation since `tf.gather` and `tf.gather_nd` need the
    # mapping from each index `i` to the index that maps to `i`.
    permutation_indices_inv = array_ops.invert_permutation(permutation_indices)
    matrix = array_ops.gather(matrix, permutation_indices_inv, axis=0)
    matrix = array_ops.gather(matrix, permutation_indices_inv, axis=1)
elif matrix.shape.ndims == 3:
    permutation_indices_inv = map_fn.map_fn(array_ops.invert_permutation,
                                            permutation_indices)
    # For 3D Tensors, it's easy to shuffle the rows but not the columns. We
    # permute the rows, transpose, permute the rows again, and transpose back.
    batch_size = matrix.shape[0]
    batch_indices = array_ops.broadcast_to(
        math_ops.range(batch_size)[:, None], permutation_indices.shape)
    for _ in range(2):
        matrix = array_ops.gather_nd(
            matrix,
            array_ops.stack([batch_indices, permutation_indices_inv], axis=-1))
        # Transpose the matrix, or equivalently, swap dimensions 1 and 2.
        matrix = array_ops.transpose(matrix, perm=[0, 2, 1])
else:
    raise ValueError("Input matrix must have rank 2 or 3. Got: {}".format(
        matrix.shape.ndims))

exit(matrix)
