# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
# Verify that Px = LU.
lu, perm = linalg_ops.lu(x, output_idx_type=output_idx_type)

# Prepare the lower factor of shape num_rows x num_rows
lu_shape = np.array(lu.shape.as_list())
batch_shape = lu_shape[:-2]
num_rows = lu_shape[-2]
num_cols = lu_shape[-1]

lower = array_ops.matrix_band_part(lu, -1, 0)

if num_rows > num_cols:
    eye = linalg_ops.eye(
        num_rows, batch_shape=batch_shape, dtype=lower.dtype)
    lower = array_ops.concat([lower, eye[..., num_cols:]], axis=-1)
elif num_rows < num_cols:
    lower = lower[..., :num_rows]

# Fill the diagonal with ones.
ones_diag = array_ops.ones(
    np.append(batch_shape, num_rows), dtype=lower.dtype)
lower = array_ops.matrix_set_diag(lower, ones_diag)

# Prepare the upper factor.
upper = array_ops.matrix_band_part(lu, 0, -1)

verification = test_util.matmul_without_tf32(lower, upper)

# Permute the rows of product of the Cholesky factors.
if num_rows > 0:
    # Reshape the product of the triangular factors and permutation indices
    # to a single batch dimension. This makes it easy to apply
    # invert_permutation and gather_nd ops.
    perm_reshaped = array_ops.reshape(perm, [-1, num_rows])
    verification_reshaped = array_ops.reshape(verification,
                                              [-1, num_rows, num_cols])
    # Invert the permutation in each batch.
    inv_perm_reshaped = map_fn.map_fn(array_ops.invert_permutation,
                                      perm_reshaped)
    batch_size = perm_reshaped.shape.as_list()[0]
    # Prepare the batch indices with the same shape as the permutation.
    # The corresponding batch index is paired with each of the `num_rows`
    # permutation indices.
    batch_indices = math_ops.cast(
        array_ops.broadcast_to(
            math_ops.range(batch_size)[:, None], perm_reshaped.shape),
        dtype=output_idx_type)
    if inv_perm_reshaped.shape == [0]:
        inv_perm_reshaped = array_ops.zeros_like(batch_indices)
    permuted_verification_reshaped = array_ops.gather_nd(
        verification_reshaped,
        array_ops.stack([batch_indices, inv_perm_reshaped], axis=-1))

    # Reshape the verification matrix back to the original shape.
    verification = array_ops.reshape(permuted_verification_reshaped,
                                     lu_shape)

self._verifyLuBase(x, lower, upper, perm, verification,
                   output_idx_type)
