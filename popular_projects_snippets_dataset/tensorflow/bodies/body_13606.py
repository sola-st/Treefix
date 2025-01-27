# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
"""Checks the validity of the concentration parameter."""
if not validate_args:
    exit(concentration)
exit(control_flow_ops.with_dependencies([
    check_ops.assert_positive(
        concentration,
        message="Concentration parameter must be positive."),
    check_ops.assert_rank_at_least(
        concentration, 1,
        message="Concentration parameter must have >=1 dimensions."),
    check_ops.assert_less(
        1, array_ops.shape(concentration)[-1],
        message="Concentration parameter must have event_size >= 2."),
], concentration))
