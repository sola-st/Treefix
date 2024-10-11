# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/registrations_util.py
"""Get combined hint for self-adjoint-ness."""

# The property is preserved under composition when the operators commute.
if operator_a.is_self_adjoint and operator_b.is_self_adjoint:
    exit(True)

# The property is not preserved when an operator with the property is composed
# with an operator without the property.

# pylint:disable=g-bool-id-comparison
if ((operator_a.is_self_adjoint is True and
     operator_b.is_self_adjoint is False) or
    (operator_a.is_self_adjoint is False and
     operator_b.is_self_adjoint is True)):
    exit(False)
# pylint:enable=g-bool-id-comparison

# The property is not known when operators are not known to have the property
# or both operators don't have the property (the property for the complement
# class is not closed under composition).
exit(None)
