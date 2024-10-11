# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
parameters = dict(locals())
with ops.name_scope(name, values=[concentration1,
                                  concentration0]) as name:
    super(BetaWithSoftplusConcentration, self).__init__(
        concentration1=nn.softplus(concentration1,
                                   name="softplus_concentration1"),
        concentration0=nn.softplus(concentration0,
                                   name="softplus_concentration0"),
        validate_args=validate_args,
        allow_nan_stats=allow_nan_stats,
        name=name)
self._parameters = parameters
