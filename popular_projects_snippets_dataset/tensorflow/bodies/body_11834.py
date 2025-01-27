# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
r"""Solve triangular systems of equations with a banded solver.

  `bands` is a tensor of shape `[..., K, M]`, where `K` represents the number
  of bands stored. This corresponds to a batch of `M` by `M` matrices, whose
  `K` subdiagonals (when `lower` is `True`) are stored.

  This operator broadcasts the batch dimensions of `bands` and the batch
  dimensions of `rhs`.


  Examples:

  Storing 2 bands of a 3x3 matrix.
  Note that first element in the second row is ignored due to
  the 'LEFT_RIGHT' padding.

  >>> x = [[2., 3., 4.], [1., 2., 3.]]
  >>> x2 = [[2., 3., 4.], [10000., 2., 3.]]
  >>> y = tf.zeros([3, 3])
  >>> z = tf.linalg.set_diag(y, x, align='LEFT_RIGHT', k=(-1, 0))
  >>> z
  <tf.Tensor: shape=(3, 3), dtype=float32, numpy=
  array([[2., 0., 0.],
         [2., 3., 0.],
         [0., 3., 4.]], dtype=float32)>
  >>> soln = tf.linalg.banded_triangular_solve(x, tf.ones([3, 1]))
  >>> soln
  <tf.Tensor: shape=(3, 1), dtype=float32, numpy=
  array([[0.5 ],
         [0.  ],
         [0.25]], dtype=float32)>
  >>> are_equal = soln == tf.linalg.banded_triangular_solve(x2, tf.ones([3, 1]))
  >>> tf.reduce_all(are_equal).numpy()
  True
  >>> are_equal = soln == tf.linalg.triangular_solve(z, tf.ones([3, 1]))
  >>> tf.reduce_all(are_equal).numpy()
  True

  Storing 2 superdiagonals of a 4x4 matrix. Because of the 'LEFT_RIGHT' padding
  the last element of the first row is ignored.

  >>> x = [[2., 3., 4., 5.], [-1., -2., -3., -4.]]
  >>> y = tf.zeros([4, 4])
  >>> z = tf.linalg.set_diag(y, x, align='LEFT_RIGHT', k=(0, 1))
  >>> z
  <tf.Tensor: shape=(4, 4), dtype=float32, numpy=
  array([[-1.,  2.,  0.,  0.],
         [ 0., -2.,  3.,  0.],
         [ 0.,  0., -3.,  4.],
         [ 0.,  0., -0., -4.]], dtype=float32)>
  >>> soln = tf.linalg.banded_triangular_solve(x, tf.ones([4, 1]), lower=False)
  >>> soln
  <tf.Tensor: shape=(4, 1), dtype=float32, numpy=
  array([[-4.       ],
         [-1.5      ],
         [-0.6666667],
         [-0.25     ]], dtype=float32)>
  >>> are_equal = (soln == tf.linalg.triangular_solve(
  ...   z, tf.ones([4, 1]), lower=False))
  >>> tf.reduce_all(are_equal).numpy()
  True


  Args:
    bands: A `Tensor` describing the bands of the left hand side, with shape
      `[..., K, M]`. The `K` rows correspond to the diagonal to the `K - 1`-th
      diagonal (the diagonal is the top row) when `lower` is `True` and
      otherwise the `K - 1`-th superdiagonal to the diagonal (the diagonal is
      the bottom row) when `lower` is `False`. The bands are stored with
      'LEFT_RIGHT' alignment, where the superdiagonals are padded on the right
      and subdiagonals are padded on the left. This is the alignment cuSPARSE
      uses.  See  `tf.linalg.set_diag` for more details.
    rhs: A `Tensor` of shape [..., M] or [..., M, N] and with the same dtype as
      `diagonals`. Note that if the shape of `rhs` and/or `diags` isn't known
      statically, `rhs` will be treated as a matrix rather than a vector.
    lower: An optional `bool`. Defaults to `True`. Boolean indicating whether
      `bands` represents a lower or upper triangular matrix.
    adjoint: An optional `bool`. Defaults to `False`. Boolean indicating whether
      to solve with the matrix's block-wise adjoint.
    name:  A name to give this `Op` (optional).

  Returns:
    A `Tensor` of shape [..., M] or [..., M, N] containing the solutions.
  """
with ops.name_scope(name, 'banded_triangular_solve', [bands, rhs]):
    exit(gen_linalg_ops.banded_triangular_solve(
        bands, rhs, lower=lower, adjoint=adjoint))
