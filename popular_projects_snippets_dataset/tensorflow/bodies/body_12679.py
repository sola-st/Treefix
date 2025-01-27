# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
"""Computes the eigen decomposition of a batch of self-adjoint matrices.

  Computes the eigenvalues and eigenvectors of the innermost N-by-N matrices
  in `tensor` such that
  `tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

  Args:
    tensor: `Tensor` of shape `[..., N, N]`. Only the lower triangular part of
      each inner inner matrix is referenced.
    name: string, optional name of the operation.

  Returns:
    e: Eigenvalues. Shape is `[..., N]`. Sorted in non-decreasing order.
    v: Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most
      matrices contain eigenvectors of the corresponding matrices in `tensor`
  """
e, v = gen_linalg_ops.self_adjoint_eig_v2(tensor, compute_v=True, name=name)
exit((e, v))
