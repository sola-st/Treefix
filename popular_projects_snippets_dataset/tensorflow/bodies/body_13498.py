# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
"""Initialize a batch of Multinomial distributions.

    Args:
      total_count: Non-negative floating point tensor with shape broadcastable
        to `[N1,..., Nm]` with `m >= 0`. Defines this as a batch of
        `N1 x ... x Nm` different Multinomial distributions. Its components
        should be equal to integer values.
      logits: Floating point tensor representing unnormalized log-probabilities
        of a positive event with shape broadcastable to
        `[N1,..., Nm, K]` `m >= 0`, and the same dtype as `total_count`. Defines
        this as a batch of `N1 x ... x Nm` different `K` class Multinomial
        distributions. Only one of `logits` or `probs` should be passed in.
      probs: Positive floating point tensor with shape broadcastable to
        `[N1,..., Nm, K]` `m >= 0` and same dtype as `total_count`. Defines
        this as a batch of `N1 x ... x Nm` different `K` class Multinomial
        distributions. `probs`'s components in the last portion of its shape
        should sum to `1`. Only one of `logits` or `probs` should be passed in.
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
with ops.name_scope(name, values=[total_count, logits, probs]) as name:
    self._total_count = ops.convert_to_tensor(total_count, name="total_count")
    if validate_args:
        self._total_count = (
            distribution_util.embed_check_nonnegative_integer_form(
                self._total_count))
    self._logits, self._probs = distribution_util.get_logits_and_probs(
        logits=logits,
        probs=probs,
        multidimensional=True,
        validate_args=validate_args,
        name=name)
    self._mean_val = self._total_count[..., array_ops.newaxis] * self._probs
super(Multinomial, self).__init__(
    dtype=self._probs.dtype,
    reparameterization_type=distribution.NOT_REPARAMETERIZED,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    parameters=parameters,
    graph_parents=[self._total_count,
                   self._logits,
                   self._probs],
    name=name)
