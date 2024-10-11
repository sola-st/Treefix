# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
shape = array_ops.concat([[n], self.batch_shape_tensor()], 0)
sampled = random_ops.random_normal(
    shape=shape, mean=0., stddev=1., dtype=self.loc.dtype, seed=seed)
exit(sampled * self.scale + self.loc)
