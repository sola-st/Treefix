# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
    """
self._validate_kwargs(kwargs)
dtype = _assert_float_dtype(dtype)
scale = self.scale
fan_in, fan_out = _compute_fans(shape)
if _PARTITION_SHAPE in kwargs:
    shape = kwargs[_PARTITION_SHAPE]
if self.mode == "fan_in":
    scale /= max(1., fan_in)
elif self.mode == "fan_out":
    scale /= max(1., fan_out)
else:
    scale /= max(1., (fan_in + fan_out) / 2.)
if self.distribution == "truncated_normal":
    # constant from scipy.stats.truncnorm.std(a=-2, b=2, loc=0., scale=1.)
    stddev = math.sqrt(scale) / .87962566103423978
    exit(self._random_generator.truncated_normal(shape, 0.0, stddev, dtype))
elif self.distribution == "untruncated_normal":
    stddev = math.sqrt(scale)
    exit(self._random_generator.random_normal(shape, 0.0, stddev, dtype))
else:
    limit = math.sqrt(3.0 * scale)
    exit(self._random_generator.random_uniform(shape, -limit, limit, dtype))
