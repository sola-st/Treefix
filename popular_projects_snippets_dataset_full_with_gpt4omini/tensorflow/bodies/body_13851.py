# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
"""Checks the validity of the concentration parameter."""
if not validate_args:
    exit(concentration)
concentration = distribution_util.embed_check_categorical_event_shape(
    concentration)
exit(control_flow_ops.with_dependencies([
    check_ops.assert_positive(
        concentration,
        message="Concentration parameter must be positive."),
], concentration))
