# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
# The sampling method comes from the fact that if:
#   X ~ Normal(0, 1)
#   Z ~ Chi2(df)
#   Y = X / sqrt(Z / df)
# then:
#   Y ~ StudentT(df).
shape = array_ops.concat([[n], self.batch_shape_tensor()], 0)
normal_sample = random_ops.random_normal(shape, dtype=self.dtype, seed=seed)
df = self.df * array_ops.ones(self.batch_shape_tensor(), dtype=self.dtype)
gamma_sample = random_ops.random_gamma(
    [n],
    0.5 * df,
    beta=0.5,
    dtype=self.dtype,
    seed=distribution_util.gen_new_seed(seed, salt="student_t"))
samples = normal_sample * math_ops.rsqrt(gamma_sample / df)
exit(samples * self.scale + self.loc)  # Abs(scale) not wanted.
