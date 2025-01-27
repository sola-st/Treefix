# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/categorical.py
"""Initialize Categorical distributions using class log-probabilities.

    Args:
      logits: An N-D `Tensor`, `N >= 1`, representing the log probabilities
        of a set of Categorical distributions. The first `N - 1` dimensions
        index into a batch of independent distributions and the last dimension
        represents a vector of logits for each class. Only one of `logits` or
        `probs` should be passed in.
      probs: An N-D `Tensor`, `N >= 1`, representing the probabilities
        of a set of Categorical distributions. The first `N - 1` dimensions
        index into a batch of independent distributions and the last dimension
        represents a vector of probabilities for each class. Only one of
        `logits` or `probs` should be passed in.
      dtype: The type of the event samples (default: int32).
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
with ops.name_scope(name, values=[logits, probs]) as name:
    self._logits, self._probs = distribution_util.get_logits_and_probs(
        logits=logits,
        probs=probs,
        validate_args=validate_args,
        multidimensional=True,
        name=name)

    if validate_args:
        self._logits = distribution_util.embed_check_categorical_event_shape(
            self._logits)

    logits_shape_static = self._logits.get_shape().with_rank_at_least(1)
    if logits_shape_static.ndims is not None:
        self._batch_rank = ops.convert_to_tensor(
            logits_shape_static.ndims - 1,
            dtype=dtypes.int32,
            name="batch_rank")
    else:
        with ops.name_scope(name="batch_rank"):
            self._batch_rank = array_ops.rank(self._logits) - 1

    logits_shape = array_ops.shape(self._logits, name="logits_shape")
    if tensor_shape.dimension_value(logits_shape_static[-1]) is not None:
        self._event_size = ops.convert_to_tensor(
            logits_shape_static.dims[-1].value,
            dtype=dtypes.int32,
            name="event_size")
    else:
        with ops.name_scope(name="event_size"):
            self._event_size = logits_shape[self._batch_rank]

    if logits_shape_static[:-1].is_fully_defined():
        self._batch_shape_val = constant_op.constant(
            logits_shape_static[:-1].as_list(),
            dtype=dtypes.int32,
            name="batch_shape")
    else:
        with ops.name_scope(name="batch_shape"):
            self._batch_shape_val = logits_shape[:-1]
super(Categorical, self).__init__(
    dtype=dtype,
    reparameterization_type=distribution.NOT_REPARAMETERIZED,
    validate_args=validate_args,
    allow_nan_stats=allow_nan_stats,
    parameters=parameters,
    graph_parents=[self._logits,
                   self._probs],
    name=name)
