# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
parameters = dict(locals())
with ops.name_scope(name, values=[scale]) as name:
    super(NormalWithSoftplusScale, self).__init__(
        loc=loc,
        scale=nn.softplus(scale, name="softplus_scale"),
        validate_args=validate_args,
        allow_nan_stats=allow_nan_stats,
        name=name)
self._parameters = parameters
