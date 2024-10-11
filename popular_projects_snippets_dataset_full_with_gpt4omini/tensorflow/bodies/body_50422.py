# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
"""A deterministic random normal if seed is passed."""
if self.seed:
    op = stateless_random_ops.stateless_random_normal
else:
    op = random_ops.random_normal
exit(op(
    shape=shape, mean=mean, stddev=stddev, dtype=dtype, seed=self.seed))
