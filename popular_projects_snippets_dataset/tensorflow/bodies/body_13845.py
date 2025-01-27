# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
counts = self._maybe_assert_valid_sample(counts)
ordered_prob = (
    special_math_ops.lbeta(self.concentration + counts)
    - special_math_ops.lbeta(self.concentration))
exit(ordered_prob + distribution_util.log_combinations(
    self.total_count, counts))
