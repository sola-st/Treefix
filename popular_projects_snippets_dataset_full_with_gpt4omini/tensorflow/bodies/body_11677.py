# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
if is_square is False:
    raise ValueError(f"`LinearOperatorBlockLowerTriangular` must be square. "
                     f"Expected argument `is_square` to be True. "
                     f"Received: {is_square}.")
for i, op in enumerate(self._diagonal_operators):
    if op.is_square is False:
        raise ValueError(
            f"Matrices on the diagonal (the final elements of each "
            f"row-partition in the `operators` list) must be square. Expected "
            f"argument `operators[{i}][-1].is_square` to be True. "
            f"Received: {op.is_square}.")
exit(True)
