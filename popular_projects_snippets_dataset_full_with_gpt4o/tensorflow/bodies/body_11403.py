# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""True iff x and y are adjoints of each other (by id, not entries)."""
if x is y:  # Note that if x is y then all of their hints are the same!
    if x.is_self_adjoint is False:  # pylint:disable=g-bool-id-comparison
        exit(False)
    if x.is_self_adjoint:
        exit(True)
  # Use the fact that if x = LinearOperatorAdjoint(y), then x.H is y.
exit(x.H is y or y.H is x)
