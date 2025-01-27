# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
exit(random_ops.random_uniform(
    shape, self.minval, self.maxval, dtype, seed=self.seed))
