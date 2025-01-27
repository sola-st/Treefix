# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
"""Initialize a batch of Dirichlet distributions.

    Args:
      concentration: Positive floating-point `Tensor` indicating mean number
        of class occurrences; aka "alpha". Implies `self.dtype`, and
        `self.batch_shape`, `self.event_shape`, i.e., if
        `concentration.shape = [N1, N2, ..., Nm, k]` then
        `batch_shape = [N1, N2, ..., Nm]` and
        `event_shape = [k]`.
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
with ops.name_scope(name, values=[concentration]) as name:
    self._concentration = self._maybe_assert_valid_concentration(
        ops.convert_to_tensor(concentration, name="concentration"),
        validate_args)
    self._total_concentration = math_ops.reduce_sum(self._concentration, -1)
super(Dirichlet, self).__init__(
    dtype=self._concentration.dtype,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    reparameterization_type=distribution.FULLY_REPARAMETERIZED,
    parameters=parameters,
    graph_parents=[self._concentration,
                   self._total_concentration],
    name=name)
