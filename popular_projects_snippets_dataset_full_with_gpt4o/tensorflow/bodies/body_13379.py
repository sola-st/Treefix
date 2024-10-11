# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Multiplies matrices and extracts three diagonals from the product.

  With sizes M x K and K x M, this function takes O(MK) time and O(M) space,
  while using math_ops.matmul, and then extracting the diagonals would take
  O(M^2 K) time and O(M^2) space.

  Args:
    x: first matrix
    y_tr: second matrix transposed

  Returns:
    Diagonals of the product in compact format (see
    linalg_ops.tridiagonal_solve)

  """
diag = math_ops.reduce_sum(x * y_tr, axis=-1)

if y_tr.shape.is_fully_defined():
    zeros = array_ops.zeros(
        list(x.shape[:-2]) + [1, x.shape[-1]], dtype=x.dtype)
    superdiag = math_ops.reduce_sum(
        x * array_ops.concat((y_tr[..., 1:, :], zeros), axis=-2), axis=-1)
    subdiag = math_ops.reduce_sum(
        x * array_ops.concat((zeros, y_tr[..., :-1, :]), axis=-2), axis=-1)
else:
    rank = array_ops.rank(y_tr)
    zeros = array_ops.zeros((rank - 2, 2), dtype=dtypes.int32)
    superdiag_pad = array_ops.concat(
        (zeros, array_ops.constant([[0, 1], [0, 0]])), axis=0)
    superdiag = math_ops.reduce_sum(
        x * array_ops.pad(y_tr[..., 1:, :], superdiag_pad), axis=-1)
    subdiag_pad = array_ops.concat(
        (zeros, array_ops.constant([[1, 0], [0, 0]])), axis=0)
    subdiag = math_ops.reduce_sum(
        x * array_ops.pad(y_tr[..., :-1, :], subdiag_pad), axis=-1)
exit(array_ops.stack([superdiag, diag, subdiag], axis=-2))
