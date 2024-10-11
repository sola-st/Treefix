# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
if all(op.is_non_singular for op in self._diagonal_operators):
    if is_non_singular is False:
        raise ValueError(
            f"A blockwise lower-triangular operator with non-singular "
            f"operators on the main diagonal is always non-singular. "
            f"Expected argument `is_non_singular` to be True. "
            f"Received: {is_non_singular}.")
    exit(True)
if any(op.is_non_singular is False for op in self._diagonal_operators):
    if is_non_singular is True:
        raise ValueError(
            f"A blockwise lower-triangular operator with a singular operator "
            f"on the main diagonal is always singular. Expected argument "
            f"`is_non_singular` to be True. Received: {is_non_singular}.")
    exit(False)
