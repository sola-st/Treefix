# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""A deterministic truncated normal if seed is passed."""
if self.seed:
    op = stateless_random_ops.stateless_truncated_normal
else:
    op = random_ops.truncated_normal
exit(op(
    shape=shape, mean=mean, stddev=stddev, dtype=dtype, seed=self.seed))
