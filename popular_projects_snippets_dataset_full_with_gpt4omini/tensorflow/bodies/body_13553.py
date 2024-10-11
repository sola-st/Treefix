# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bernoulli.py
new_shape = array_ops.concat([[n], self.batch_shape_tensor()], 0)
uniform = random_ops.random_uniform(
    new_shape, seed=seed, dtype=self.probs.dtype)
sample = math_ops.less(uniform, self.probs)
exit(math_ops.cast(sample, self.dtype))
