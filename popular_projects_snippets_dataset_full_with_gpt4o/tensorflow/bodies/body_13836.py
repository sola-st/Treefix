# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
"""Initialize a batch of DirichletMultinomial distributions.

    Args:
      total_count:  Non-negative floating point tensor, whose dtype is the same
        as `concentration`. The shape is broadcastable to `[N1,..., Nm]` with
        `m >= 0`. Defines this as a batch of `N1 x ... x Nm` different
        Dirichlet multinomial distributions. Its components should be equal to
        integer values.
      concentration: Positive floating point tensor, whose dtype is the
        same as `n` with shape broadcastable to `[N1,..., Nm, K]` `m >= 0`.
        Defines this as a batch of `N1 x ... x Nm` different `K` class Dirichlet
        multinomial distributions.
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
with ops.name_scope(name, values=[total_count, concentration]) as name:
    # Broadcasting works because:
    # * The broadcasting convention is to prepend dimensions of size [1], and
    #   we use the last dimension for the distribution, whereas
    #   the batch dimensions are the leading dimensions, which forces the
    #   distribution dimension to be defined explicitly (i.e. it cannot be
    #   created automatically by prepending). This forces enough explicitness.
    # * All calls involving `counts` eventually require a broadcast between
    #  `counts` and concentration.
    self._total_count = ops.convert_to_tensor(total_count, name="total_count")
    if validate_args:
        self._total_count = (
            distribution_util.embed_check_nonnegative_integer_form(
                self._total_count))
    self._concentration = self._maybe_assert_valid_concentration(
        ops.convert_to_tensor(concentration,
                              name="concentration"),
        validate_args)
    self._total_concentration = math_ops.reduce_sum(self._concentration, -1)
super(DirichletMultinomial, self).__init__(
    dtype=self._concentration.dtype,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    reparameterization_type=distribution.NOT_REPARAMETERIZED,
    parameters=parameters,
    graph_parents=[self._total_count,
                   self._concentration],
    name=name)
