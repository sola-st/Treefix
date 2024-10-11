# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
"""Checks the validity of a concentration parameter."""
if not validate_args:
    exit(concentration)
exit(control_flow_ops.with_dependencies([
    check_ops.assert_positive(
        concentration,
        message="Concentration parameter must be positive."),
], concentration))
