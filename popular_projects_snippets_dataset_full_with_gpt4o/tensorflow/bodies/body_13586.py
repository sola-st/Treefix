# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/exponential.py
shape = array_ops.concat([[n], array_ops.shape(self._rate)], 0)
# Uniform variates must be sampled from the open-interval `(0, 1)` rather
# than `[0, 1)`. To do so, we use `np.finfo(self.dtype.as_numpy_dtype).tiny`
# because it is the smallest, positive, "normal" number. A "normal" number
# is such that the mantissa has an implicit leading 1. Normal, positive
# numbers x, y have the reasonable property that, `x + y >= max(x, y)`. In
# this case, a subnormal number (i.e., np.nextafter) can cause us to sample
# 0.
sampled = random_ops.random_uniform(
    shape,
    minval=np.finfo(self.dtype.as_numpy_dtype).tiny,
    maxval=1.,
    seed=seed,
    dtype=self.dtype)
exit(-math_ops.log(sampled) / self._rate)
