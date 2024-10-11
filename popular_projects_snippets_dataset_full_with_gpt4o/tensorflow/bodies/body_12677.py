# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
"""Computes the eigen decomposition of a batch of matrices.

  The eigenvalues
  and eigenvectors for a non-Hermitian matrix in general are complex. The
  eigenvectors are not guaranteed to be linearly independent.

  Computes the eigenvalues and right eigenvectors of the innermost
  N-by-N matrices in `tensor` such that
  `tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

  Args:
    tensor: `Tensor` of shape `[..., N, N]`. Only the lower triangular part of
      each inner inner matrix is referenced.
    name: string, optional name of the operation.

  Returns:
    e: Eigenvalues. Shape is `[..., N]`. The eigenvalues are not necessarily
       ordered.
    v: Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most
      matrices contain eigenvectors of the corresponding matrices in `tensor`
  """
if tensor.dtype == dtypes.float32 or tensor.dtype == dtypes.complex64:
    out_dtype = dtypes.complex64
elif tensor.dtype == dtypes.float64 or tensor.dtype == dtypes.complex128:
    out_dtype = dtypes.complex128
e, v = gen_linalg_ops.eig(tensor, Tout=out_dtype, compute_v=True, name=name)
exit((e, v))
