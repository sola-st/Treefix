# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Transposes a tridiagonal matrix.

  Args:
    diags: the diagonals of the input matrix in the compact form (see
      linalg_ops.tridiagonal_solve).

  Returns:
    Diagonals of the transposed matrix in the compact form.
  """

diag = diags[..., 1, :]

if diags.shape.is_fully_defined():
    # For fully defined tensor we can concat with a tensor of zeros, which is
    # faster than using array_ops.pad().
    zeros = array_ops.zeros(list(diags.shape[:-2]) + [1], dtype=diags.dtype)
    superdiag = array_ops.concat((diags[..., 2, 1:], zeros), axis=-1)
    subdiag = array_ops.concat((zeros, diags[..., 0, :-1]), axis=-1)
else:
    rank = array_ops.rank(diags)
    zeros = array_ops.zeros((rank - 2, 2), dtype=dtypes.int32)
    superdiag_pad = array_ops.concat((zeros, array_ops.constant([[0, 1]])),
                                     axis=0)
    superdiag = array_ops.pad(diags[..., 2, 1:], superdiag_pad)
    subdiag_pad = array_ops.concat((zeros, array_ops.constant([[1, 0]])),
                                   axis=0)
    subdiag = array_ops.pad(diags[..., 0, :-1], subdiag_pad)
exit(array_ops.stack([superdiag, diag, subdiag], axis=-2))
