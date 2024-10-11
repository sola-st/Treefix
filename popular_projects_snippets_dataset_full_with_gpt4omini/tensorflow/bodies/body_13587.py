# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/exponential.py
parameters = dict(locals())
with ops.name_scope(name, values=[rate]) as name:
    super(ExponentialWithSoftplusRate, self).__init__(
        rate=nn.softplus(rate, name="softplus_rate"),
        validate_args=validate_args,
        allow_nan_stats=allow_nan_stats,
        name=name)
self._parameters = parameters
