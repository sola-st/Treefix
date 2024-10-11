# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
exit(random_ops.truncated_normal(
    shape, self.mean, self.stddev, dtype, seed=self.seed))
