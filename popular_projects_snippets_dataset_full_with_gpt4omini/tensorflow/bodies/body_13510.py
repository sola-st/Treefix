# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
counts = self._maybe_assert_valid_sample(counts)
exit(-distribution_util.log_combinations(self.total_count, counts))
