# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
"""Infer hints from op1 and op2.  hints argument is an override.

  Args:
    op1:  LinearOperator
    op2:  LinearOperator
    hints:  _Hints object holding "is_X" boolean hints to use for returned
      operator.
      If some hint is None, try to set using op1 and op2.  If the
      hint is provided, ignore op1 and op2 hints.  This allows an override
      of previous hints, but does not allow forbidden hints (e.g. you still
      cannot say a real diagonal operator is not self-adjoint.

  Returns:
    _Hints object.
  """
hints = hints or _Hints()
# If A, B are self-adjoint, then so is A + B.
if hints.is_self_adjoint is None:
    is_self_adjoint = op1.is_self_adjoint and op2.is_self_adjoint
else:
    is_self_adjoint = hints.is_self_adjoint

# If A, B are positive definite, then so is A + B.
if hints.is_positive_definite is None:
    is_positive_definite = op1.is_positive_definite and op2.is_positive_definite
else:
    is_positive_definite = hints.is_positive_definite

# A positive definite operator is always non-singular.
if is_positive_definite and hints.is_positive_definite is None:
    is_non_singular = True
else:
    is_non_singular = hints.is_non_singular

exit(_Hints(
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite))
