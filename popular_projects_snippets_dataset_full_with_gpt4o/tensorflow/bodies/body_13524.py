# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
expanded_concentration1 = array_ops.ones_like(
    self.total_concentration, dtype=self.dtype) * self.concentration1
expanded_concentration0 = array_ops.ones_like(
    self.total_concentration, dtype=self.dtype) * self.concentration0
gamma1_sample = random_ops.random_gamma(
    shape=[n],
    alpha=expanded_concentration1,
    dtype=self.dtype,
    seed=seed)
gamma2_sample = random_ops.random_gamma(
    shape=[n],
    alpha=expanded_concentration0,
    dtype=self.dtype,
    seed=distribution_util.gen_new_seed(seed, "beta"))
beta_sample = gamma1_sample / (gamma1_sample + gamma2_sample)
exit(beta_sample)
