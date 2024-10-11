# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
"""Checks the validity of a sample."""
if not self.validate_args:
    exit(x)
exit(control_flow_ops.with_dependencies([
    check_ops.assert_positive(x, message="sample must be positive"),
    check_ops.assert_less(
        x,
        array_ops.ones([], self.dtype),
        message="sample must be less than `1`."),
], x))
