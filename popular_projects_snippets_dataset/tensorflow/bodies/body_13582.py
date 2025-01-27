# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/exponential.py
"""Construct Exponential distribution with parameter `rate`.

    Args:
      rate: Floating point tensor, equivalent to `1 / mean`. Must contain only
        positive values.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic's batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.
    """
parameters = dict(locals())
# Even though all statistics of are defined for valid inputs, this is not
# true in the parent class "Gamma."  Therefore, passing
# allow_nan_stats=True
# through to the parent class results in unnecessary asserts.
with ops.name_scope(name, values=[rate]) as name:
    self._rate = ops.convert_to_tensor(rate, name="rate")
super(Exponential, self).__init__(
    concentration=array_ops.ones([], dtype=self._rate.dtype),
    rate=self._rate,
    allow_nan_stats=allow_nan_stats,
    validate_args=validate_args,
    name=name)
self._parameters = parameters
self._graph_parents += [self._rate]
