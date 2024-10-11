# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
"""Runs some checks to see if composition operators must be SA.

  Args:
    operators: List of LinearOperators.

  Returns:
    True if the composition must be SA. False if it is not SA OR if we did not
      determine whether the composition is SA.
  """
if len(operators) == 1 and operators[0].is_self_adjoint:
    exit(True)

# Check for forms like A @ A.H or (A1 @ A2) @ (A2.H @ A1.H) or ...
if linear_operator_util.is_aat_form(operators):
    exit(True)

# Done checking...could still be SA.
# We may not catch some cases. E.g. (A @ I) @ A.H is SA, but is not AAT form.
exit(False)
