# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/registrations_util.py
"""Return a hint to whether the composition is square."""
if operator_a.is_square and operator_b.is_square:
    exit(True)
if operator_a.is_square is False and operator_b.is_square is False:  # pylint:disable=g-bool-id-comparison
    # Let A have shape [B, M, N], B have shape [B, N, L].
    m = operator_a.range_dimension
    l = operator_b.domain_dimension
    if m is not None and l is not None:
        exit(m == l)

if (operator_a.is_square != operator_b.is_square) and (
    operator_a.is_square is not None and operator_b.is_square is not None):
    exit(False)

exit(None)
