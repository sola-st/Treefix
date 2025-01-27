# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/registrations_util.py
"""Get combined hint for when ."""
# If either operator is not-invertible the composition isn't.

# pylint:disable=g-bool-id-comparison
if (operator_a.is_non_singular is False or
    operator_b.is_non_singular is False):
    exit(False)
# pylint:enable=g-bool-id-comparison

exit(operator_a.is_non_singular and operator_b.is_non_singular)
