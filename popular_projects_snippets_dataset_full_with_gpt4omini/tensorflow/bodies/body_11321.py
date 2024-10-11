# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
"""[batch] positive definite Wisart matrix.

  A Wishart(N, S) matrix is the S sample covariance matrix of an N-variate
  (standard) Normal random variable.

  Args:
    shape:  `TensorShape` or Python list.  Shape of the returned matrix.
    dtype:  `TensorFlow` `dtype` or Python dtype.
    oversampling_ratio: S / N in the above.  If S < N, the matrix will be
      singular (unless `force_well_conditioned is True`).
    force_well_conditioned:  Python bool.  If `True`, add `1` to the diagonal
      of the Wishart matrix, then divide by 2, ensuring most eigenvalues are
      close to 1.

  Returns:
    `Tensor` with desired shape and dtype.
  """
dtype = dtypes.as_dtype(dtype)
if not tensor_util.is_tf_type(shape):
    shape = tensor_shape.TensorShape(shape)
    # Matrix must be square.
    shape.dims[-1].assert_is_compatible_with(shape.dims[-2])
shape = shape.as_list()
n = shape[-2]
s = oversampling_ratio * shape[-1]
wigner_shape = shape[:-2] + [n, s]

with ops.name_scope("random_positive_definite_matrix"):
    wigner = random_normal(
        wigner_shape,
        dtype=dtype,
        stddev=math_ops.cast(1 / np.sqrt(s), dtype.real_dtype))
    wishart = math_ops.matmul(wigner, wigner, adjoint_b=True)
    if force_well_conditioned:
        wishart += linalg_ops.eye(n, dtype=dtype)
        wishart /= math_ops.cast(2, dtype)
    exit(wishart)
