# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""The reconstruct one or more matrices from their LU decomposition(s).

  Args:
    lower_upper: `lu` as returned by `tf.linalg.lu`, i.e., if `matmul(P,
      matmul(L, U)) = X` then `lower_upper = L + U - eye`.
    perm: `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) =
      X` then `perm = argmax(P)`.
    validate_args: Python `bool` indicating whether arguments should be checked
      for correctness.
      Default value: `False` (i.e., don't validate arguments).
    name: Python `str` name given to ops managed by this object.
      Default value: `None` (i.e., 'lu_reconstruct').

  Returns:
    x: The original input to `tf.linalg.lu`, i.e., `x` as in,
      `lu_reconstruct(*tf.linalg.lu(x))`.

  #### Examples

  ```python
  import numpy as np
  import tensorflow as tf
  import tensorflow_probability as tfp

  x = [[[3., 4], [1, 2]],
       [[7., 8], [3, 4]]]
  x_reconstructed = tf.linalg.lu_reconstruct(*tf.linalg.lu(x))
  tf.assert_near(x, x_reconstructed)
  # ==> True
  ```

  """
with ops.name_scope(name or 'lu_reconstruct'):
    lower_upper = ops.convert_to_tensor(
        lower_upper, dtype_hint=dtypes.float32, name='lower_upper')
    perm = ops.convert_to_tensor(perm, dtype_hint=dtypes.int32, name='perm')

    assertions = lu_reconstruct_assertions(lower_upper, perm, validate_args)
    if assertions:
        with ops.control_dependencies(assertions):
            lower_upper = array_ops.identity(lower_upper)
            perm = array_ops.identity(perm)

    shape = array_ops.shape(lower_upper)

    lower = set_diag(
        band_part(lower_upper, num_lower=-1, num_upper=0),
        array_ops.ones(shape[:-1], dtype=lower_upper.dtype))
    upper = band_part(lower_upper, num_lower=0, num_upper=-1)
    x = math_ops.matmul(lower, upper)

    if (lower_upper.shape is None or lower_upper.shape.rank is None or
        lower_upper.shape.rank != 2):
        # We either don't know the batch rank or there are >0 batch dims.
        batch_size = math_ops.reduce_prod(shape[:-2])
        d = shape[-1]
        x = array_ops.reshape(x, [batch_size, d, d])
        perm = array_ops.reshape(perm, [batch_size, d])
        perm = map_fn.map_fn(array_ops.invert_permutation, perm)
        batch_indices = array_ops.broadcast_to(
            math_ops.range(batch_size)[:, array_ops.newaxis], [batch_size, d])
        x = array_ops.gather_nd(x, array_ops.stack([batch_indices, perm],
                                                   axis=-1))
        x = array_ops.reshape(x, shape)
    else:
        x = array_ops.gather(x, array_ops.invert_permutation(perm))

    x.set_shape(lower_upper.shape)
    exit(x)
