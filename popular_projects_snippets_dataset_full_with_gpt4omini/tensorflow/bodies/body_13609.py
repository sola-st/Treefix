# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
"""Construct Gamma with `concentration` and `rate` parameters.

    The parameters `concentration` and `rate` must be shaped in a way that
    supports broadcasting (e.g. `concentration + rate` is a valid operation).

    Args:
      concentration: Floating point tensor, the concentration params of the
        distribution(s). Must contain only positive values.
      rate: Floating point tensor, the inverse scale params of the
        distribution(s). Must contain only positive values.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic's batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      TypeError: if `concentration` and `rate` are different dtypes.
    """
parameters = dict(locals())
with ops.name_scope(name, values=[concentration, rate]) as name:
    with ops.control_dependencies([
        check_ops.assert_positive(concentration),
        check_ops.assert_positive(rate),
    ] if validate_args else []):
        self._concentration = array_ops.identity(
            concentration, name="concentration")
        self._rate = array_ops.identity(rate, name="rate")
        check_ops.assert_same_float_dtype(
            [self._concentration, self._rate])
super(Gamma, self).__init__(
    dtype=self._concentration.dtype,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    reparameterization_type=distribution.FULLY_REPARAMETERIZED,
    parameters=parameters,
    graph_parents=[self._concentration,
                   self._rate],
    name=name)
