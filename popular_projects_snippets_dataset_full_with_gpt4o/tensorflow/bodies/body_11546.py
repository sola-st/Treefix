# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Return `True/False` depending on if this operator is square."""
# Static checks done after __init__.  Why?  Because domain/range dimension
# sometimes requires lots of work done in the derived class after init.
auto_square_check = self.domain_dimension == self.range_dimension
if self._is_square_set_or_implied_by_hints is False and auto_square_check:
    raise ValueError(
        "User set is_square hint to False, but the operator was square.")
if self._is_square_set_or_implied_by_hints is None:
    exit(auto_square_check)

exit(self._is_square_set_or_implied_by_hints)
