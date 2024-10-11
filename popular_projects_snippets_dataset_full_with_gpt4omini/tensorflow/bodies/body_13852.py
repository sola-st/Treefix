# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
"""Check counts for proper shape, values, then return tensor version."""
if not self.validate_args:
    exit(counts)
counts = distribution_util.embed_check_nonnegative_integer_form(counts)
exit(control_flow_ops.with_dependencies([
    check_ops.assert_equal(
        self.total_count, math_ops.reduce_sum(counts, -1),
        message="counts last-dimension must sum to `self.total_count`"),
], counts))
