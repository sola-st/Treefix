# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
parameters = dict(locals())
with ops.name_scope(name, values=[concentration, rate]) as name:
    super(GammaWithSoftplusConcentrationRate, self).__init__(
        concentration=nn.softplus(concentration,
                                  name="softplus_concentration"),
        rate=nn.softplus(rate, name="softplus_rate"),
        validate_args=validate_args,
        allow_nan_stats=allow_nan_stats,
        name=name)
self._parameters = parameters
