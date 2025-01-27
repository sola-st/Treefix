# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
parameters = dict(locals())
with ops.name_scope(name, values=[df, scale]) as name:
    super(StudentTWithAbsDfSoftplusScale, self).__init__(
        df=math_ops.floor(math_ops.abs(df)),
        loc=loc,
        scale=nn.softplus(scale, name="softplus_scale"),
        validate_args=validate_args,
        allow_nan_stats=allow_nan_stats,
        name=name)
self._parameters = parameters
