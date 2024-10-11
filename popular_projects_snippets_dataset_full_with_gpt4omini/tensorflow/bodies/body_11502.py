# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/registrations_util.py
"""Get combined PD hint for compositions."""
# pylint:disable=g-bool-id-comparison
if (operator_a.is_positive_definite is True and
    operator_a.is_self_adjoint is True and
    operator_b.is_positive_definite is True and
    operator_b.is_self_adjoint is True):
    exit(True)
# pylint:enable=g-bool-id-comparison

exit(None)
