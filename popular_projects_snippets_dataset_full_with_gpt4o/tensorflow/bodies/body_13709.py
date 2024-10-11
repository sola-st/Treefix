# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/laplace.py
shape = array_ops.concat([[n], self.batch_shape_tensor()], 0)
# Uniform variates must be sampled from the open-interval `(-1, 1)` rather
# than `[-1, 1)`. In the case of `(0, 1)` we'd use
# `np.finfo(self.dtype.as_numpy_dtype).tiny` because it is the smallest,
# positive, "normal" number. However, the concept of subnormality exists
# only at zero; here we need the smallest usable number larger than -1,
# i.e., `-1 + eps/2`.
uniform_samples = random_ops.random_uniform(
    shape=shape,
    minval=np.nextafter(self.dtype.as_numpy_dtype(-1.),
                        self.dtype.as_numpy_dtype(0.)),
    maxval=1.,
    dtype=self.dtype,
    seed=seed)
exit((self.loc - self.scale * math_ops.sign(uniform_samples) *
        math_ops.log1p(-math_ops.abs(uniform_samples))))
