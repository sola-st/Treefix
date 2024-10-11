# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
"""Initialize a batch of Beta distributions.

    Args:
      concentration1: Positive floating-point `Tensor` indicating mean
        number of successes; aka "alpha". Implies `self.dtype` and
        `self.batch_shape`, i.e.,
        `concentration1.shape = [N1, N2, ..., Nm] = self.batch_shape`.
      concentration0: Positive floating-point `Tensor` indicating mean
        number of failures; aka "beta". Otherwise has same semantics as
        `concentration1`.
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
with ops.name_scope(name, values=[concentration1, concentration0]) as name:
    self._concentration1 = self._maybe_assert_valid_concentration(
        ops.convert_to_tensor(concentration1, name="concentration1"),
        validate_args)
    self._concentration0 = self._maybe_assert_valid_concentration(
        ops.convert_to_tensor(concentration0, name="concentration0"),
        validate_args)
    check_ops.assert_same_float_dtype([
        self._concentration1, self._concentration0])
    self._total_concentration = self._concentration1 + self._concentration0
super(Beta, self).__init__(
    dtype=self._total_concentration.dtype,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    reparameterization_type=distribution.FULLY_REPARAMETERIZED,
    parameters=parameters,
    graph_parents=[self._concentration1,
                   self._concentration0,
                   self._total_concentration],
    name=name)
