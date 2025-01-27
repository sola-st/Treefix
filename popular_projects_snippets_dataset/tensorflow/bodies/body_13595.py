# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
gamma_sample = random_ops.random_gamma(
    shape=[n],
    alpha=self.concentration,
    dtype=self.dtype,
    seed=seed)
exit(gamma_sample / math_ops.reduce_sum(gamma_sample, -1, keepdims=True))
