# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
diagonal_event_ndims = 2
if self.diagonals_format == _SEQUENCE:
    # For the diagonal and the super/sub diagonals.
    diagonal_event_ndims = [1, 1, 1]
exit({
    'diagonals': diagonal_event_ndims,
})
