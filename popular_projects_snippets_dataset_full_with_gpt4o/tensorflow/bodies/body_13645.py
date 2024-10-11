# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
"""Construct Normal distributions with mean and stddev `loc` and `scale`.

    The parameters `loc` and `scale` must be shaped in a way that supports
    broadcasting (e.g. `loc + scale` is a valid operation).

    Args:
      loc: Floating point tensor; the means of the distribution(s).
      scale: Floating point tensor; the stddevs of the distribution(s).
        Must contain only positive values.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`,
        statistics (e.g., mean, mode, variance) use the value "`NaN`" to
        indicate the result is undefined. When `False`, an exception is raised
        if one or more of the statistic's batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      TypeError: if `loc` and `scale` have different `dtype`.
    """
parameters = dict(locals())
with ops.name_scope(name, values=[loc, scale]) as name:
    with ops.control_dependencies([check_ops.assert_positive(scale)] if
                                  validate_args else []):
        self._loc = array_ops.identity(loc, name="loc")
        self._scale = array_ops.identity(scale, name="scale")
        check_ops.assert_same_float_dtype([self._loc, self._scale])
super(Normal, self).__init__(
    dtype=self._scale.dtype,
    reparameterization_type=distribution.FULLY_REPARAMETERIZED,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    parameters=parameters,
    graph_parents=[self._loc, self._scale],
    name=name)
