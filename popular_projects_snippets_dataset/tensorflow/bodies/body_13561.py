# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
"""Initialize a batch of Uniform distributions.

    Args:
      low: Floating point tensor, lower boundary of the output interval. Must
        have `low < high`.
      high: Floating point tensor, upper boundary of the output interval. Must
        have `low < high`.
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
      InvalidArgumentError: if `low >= high` and `validate_args=False`.
    """
parameters = dict(locals())
with ops.name_scope(name, values=[low, high]) as name:
    with ops.control_dependencies([
        check_ops.assert_less(
            low, high, message="uniform not defined when low >= high.")
    ] if validate_args else []):
        self._low = array_ops.identity(low, name="low")
        self._high = array_ops.identity(high, name="high")
        check_ops.assert_same_float_dtype([self._low, self._high])
super(Uniform, self).__init__(
    dtype=self._low.dtype,
    reparameterization_type=distribution.FULLY_REPARAMETERIZED,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    parameters=parameters,
    graph_parents=[self._low,
                   self._high],
    name=name)
