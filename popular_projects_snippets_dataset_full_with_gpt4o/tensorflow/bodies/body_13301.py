# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
scale = self.scale
scale_shape = shape
if partition_info is not None:
    scale_shape = partition_info.full_shape
fan_in, fan_out = _compute_fans(scale_shape)
if self.mode == "fan_in":
    scale /= max(1., fan_in)
elif self.mode == "fan_out":
    scale /= max(1., fan_out)
else:
    scale /= max(1., (fan_in + fan_out) / 2.)
if self.distribution == "normal" or self.distribution == "truncated_normal":
    # constant taken from scipy.stats.truncnorm.std(a=-2, b=2, loc=0., scale=1.)
    stddev = math.sqrt(scale) / .87962566103423978
    exit(random_ops.truncated_normal(
        shape, 0.0, stddev, dtype, seed=self.seed))
elif self.distribution == "untruncated_normal":
    stddev = math.sqrt(scale)
    exit(random_ops.random_normal(shape, 0.0, stddev, dtype, seed=self.seed))
else:
    limit = math.sqrt(3.0 * scale)
    exit(random_ops.random_uniform(
        shape, -limit, limit, dtype, seed=self.seed))
