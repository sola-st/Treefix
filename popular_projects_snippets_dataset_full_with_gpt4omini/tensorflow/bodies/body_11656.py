# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
assert isinstance(matrix, ops.Tensor) and matrix.dtype == dtypes.variant
ret = type(self).__new__(type(self))
# pylint: disable=protected-access
ret._dtype = self._dtype
if self._eager_mode:
    if matrix._handle_data is None:
        matrix._handle_data = handle_data
    assert matrix._handle_data is not None
ret._csr_matrix = matrix
# pylint: enable=protected-access
exit(ret)
