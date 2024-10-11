# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Solves systems of linear eqns `A X = RHS`, given LU factorizations.

  Note: this function does not verify the implied matrix is actually invertible
  nor is this condition checked even when `validate_args=True`.

  Args:
    lower_upper: `lu` as returned by `tf.linalg.lu`, i.e., if `matmul(P,
      matmul(L, U)) = X` then `lower_upper = L + U - eye`.
    perm: `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) =
      X` then `perm = argmax(P)`.
    rhs: Matrix-shaped float `Tensor` representing targets for which to solve;
      `A X = RHS`. To handle vector cases, use: `lu_solve(..., rhs[...,
        tf.newaxis])[..., 0]`.
    validate_args: Python `bool` indicating whether arguments should be checked
      for correctness. Note: this function does not verify the implied matrix is
        actually invertible, even when `validate_args=True`.
      Default value: `False` (i.e., don't validate arguments).
    name: Python `str` name given to ops managed by this object.
      Default value: `None` (i.e., 'lu_solve').

  Returns:
    x: The `X` in `A @ X = RHS`.

  #### Examples

  ```python
  import numpy as np
  import tensorflow as tf
  import tensorflow_probability as tfp

  x = [[[1., 2],
        [3, 4]],
       [[7, 8],
        [3, 4]]]
  inv_x = tf.linalg.lu_solve(*tf.linalg.lu(x), rhs=tf.eye(2))
  tf.assert_near(tf.matrix_inverse(x), inv_x)
  # ==> True
  ```

  """

with ops.name_scope(name or 'lu_solve'):
    lower_upper = ops.convert_to_tensor(
        lower_upper, dtype_hint=dtypes.float32, name='lower_upper')
    perm = ops.convert_to_tensor(perm, dtype_hint=dtypes.int32, name='perm')
    rhs = ops.convert_to_tensor(rhs, dtype_hint=lower_upper.dtype, name='rhs')

    assertions = _lu_solve_assertions(lower_upper, perm, rhs, validate_args)
    if assertions:
        with ops.control_dependencies(assertions):
            lower_upper = array_ops.identity(lower_upper)
            perm = array_ops.identity(perm)
            rhs = array_ops.identity(rhs)

    if (rhs.shape.rank == 2 and perm.shape.rank == 1):
        # Both rhs and perm have scalar batch_shape.
        permuted_rhs = array_ops.gather(rhs, perm, axis=-2)
    else:
        # Either rhs or perm have non-scalar batch_shape or we can't determine
        # this information statically.
        rhs_shape = array_ops.shape(rhs)
        broadcast_batch_shape = array_ops.broadcast_dynamic_shape(
            rhs_shape[:-2],
            array_ops.shape(perm)[:-1])
        d, m = rhs_shape[-2], rhs_shape[-1]
        rhs_broadcast_shape = array_ops.concat([broadcast_batch_shape, [d, m]],
                                               axis=0)

        # Tile out rhs.
        broadcast_rhs = array_ops.broadcast_to(rhs, rhs_broadcast_shape)
        broadcast_rhs = array_ops.reshape(broadcast_rhs, [-1, d, m])

        # Tile out perm and add batch indices.
        broadcast_perm = array_ops.broadcast_to(perm, rhs_broadcast_shape[:-1])
        broadcast_perm = array_ops.reshape(broadcast_perm, [-1, d])
        broadcast_batch_size = math_ops.reduce_prod(broadcast_batch_shape)
        broadcast_batch_indices = array_ops.broadcast_to(
            math_ops.range(broadcast_batch_size)[:, array_ops.newaxis],
            [broadcast_batch_size, d])
        broadcast_perm = array_ops.stack(
            [broadcast_batch_indices, broadcast_perm], axis=-1)

        permuted_rhs = array_ops.gather_nd(broadcast_rhs, broadcast_perm)
        permuted_rhs = array_ops.reshape(permuted_rhs, rhs_broadcast_shape)

    lower = set_diag(
        band_part(lower_upper, num_lower=-1, num_upper=0),
        array_ops.ones(
            array_ops.shape(lower_upper)[:-1], dtype=lower_upper.dtype))
    exit(triangular_solve(
        lower_upper,  # Only upper is accessed.
        triangular_solve(lower, permuted_rhs),
        lower=False))
