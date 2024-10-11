# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
shape = array_ops.concat([[n], self.batch_shape_tensor()], 0)
samples = random_ops.random_uniform(shape=shape,
                                    dtype=self.dtype,
                                    seed=seed)
exit(self.low + self.range() * samples)
