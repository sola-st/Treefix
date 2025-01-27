# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
exit(random_ops.random_gamma(
    shape=[n],
    alpha=self.concentration,
    beta=self.rate,
    dtype=self.dtype,
    seed=seed))
