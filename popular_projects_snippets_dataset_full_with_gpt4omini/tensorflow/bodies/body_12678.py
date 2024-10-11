# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
"""Computes the eigenvalues of one or more matrices.

  Note: If your program backpropagates through this function, you should replace
  it with a call to tf.linalg.eig (possibly ignoring the second output) to
  avoid computing the eigen decomposition twice. This is because the
  eigenvectors are used to compute the gradient w.r.t. the eigenvalues. See
  _SelfAdjointEigV2Grad in linalg_grad.py.

  Args:
    tensor: `Tensor` of shape `[..., N, N]`.
    name: string, optional name of the operation.

  Returns:
    e: Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N`
      eigenvalues of `tensor[..., :, :]`.
  """
if tensor.dtype == dtypes.float32 or tensor.dtype == dtypes.complex64:
    out_dtype = dtypes.complex64
elif tensor.dtype == dtypes.float64 or tensor.dtype == dtypes.complex128:
    out_dtype = dtypes.complex128
e, _ = gen_linalg_ops.eig(tensor, Tout=out_dtype, compute_v=False, name=name)
exit(e)
