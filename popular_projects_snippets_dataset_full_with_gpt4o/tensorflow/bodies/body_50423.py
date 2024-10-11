# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
"""A deterministic random uniform if seed is passed."""
if self.seed:
    op = stateless_random_ops.stateless_random_uniform
else:
    op = random_ops.random_uniform
exit(op(
    shape=shape, minval=minval, maxval=maxval, dtype=dtype, seed=self.seed))
