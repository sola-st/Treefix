# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
"""Construct Student's t distributions.

    The distributions have degree of freedom `df`, mean `loc`, and scale
    `scale`.

    The parameters `df`, `loc`, and `scale` must be shaped in a way that
    supports broadcasting (e.g. `df + loc + scale` is a valid operation).

    Args:
      df: Floating-point `Tensor`. The degrees of freedom of the
        distribution(s). `df` must contain only positive values.
      loc: Floating-point `Tensor`. The mean(s) of the distribution(s).
      scale: Floating-point `Tensor`. The scaling factor(s) for the
        distribution(s). Note that `scale` is not technically the standard
        deviation of this distribution but has semantics more similar to
        standard deviation than variance.
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
      TypeError: if loc and scale are different dtypes.
    """
parameters = dict(locals())
with ops.name_scope(name, values=[df, loc, scale]) as name:
    with ops.control_dependencies([check_ops.assert_positive(df)]
                                  if validate_args else []):
        self._df = array_ops.identity(df, name="df")
        self._loc = array_ops.identity(loc, name="loc")
        self._scale = array_ops.identity(scale, name="scale")
        check_ops.assert_same_float_dtype(
            (self._df, self._loc, self._scale))
super(StudentT, self).__init__(
    dtype=self._scale.dtype,
    reparameterization_type=distribution.FULLY_REPARAMETERIZED,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    parameters=parameters,
    graph_parents=[self._df, self._loc, self._scale],
    name=name)
