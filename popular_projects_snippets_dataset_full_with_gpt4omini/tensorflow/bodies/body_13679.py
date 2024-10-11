# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Construct a Transformed Distribution.

    Args:
      distribution: The base distribution instance to transform. Typically an
        instance of `Distribution`.
      bijector: The object responsible for calculating the transformation.
        Typically an instance of `Bijector`. `None` means `Identity()`.
      batch_shape: `integer` vector `Tensor` which overrides `distribution`
        `batch_shape`; valid only if `distribution.is_scalar_batch()`.
      event_shape: `integer` vector `Tensor` which overrides `distribution`
        `event_shape`; valid only if `distribution.is_scalar_event()`.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      name: Python `str` name prefixed to Ops created by this class. Default:
        `bijector.name + distribution.name`.
    """
parameters = dict(locals())
name = name or (("" if bijector is None else bijector.name) +
                distribution.name)
with ops.name_scope(name, values=[event_shape, batch_shape]) as name:
    # For convenience we define some handy constants.
    self._zero = constant_op.constant(0, dtype=dtypes.int32, name="zero")
    self._empty = constant_op.constant([], dtype=dtypes.int32, name="empty")

    if bijector is None:
        bijector = identity_bijector.Identity(validate_args=validate_args)

    # We will keep track of a static and dynamic version of
    # self._is_{batch,event}_override. This way we can do more prior to graph
    # execution, including possibly raising Python exceptions.

    self._override_batch_shape = self._maybe_validate_shape_override(
        batch_shape, distribution.is_scalar_batch(), validate_args,
        "batch_shape")
    self._is_batch_override = _logical_not(_logical_equal(
        _ndims_from_shape(self._override_batch_shape), self._zero))
    self._is_maybe_batch_override = bool(
        tensor_util.constant_value(self._override_batch_shape) is None or
        tensor_util.constant_value(self._override_batch_shape).size != 0)

    self._override_event_shape = self._maybe_validate_shape_override(
        event_shape, distribution.is_scalar_event(), validate_args,
        "event_shape")
    self._is_event_override = _logical_not(_logical_equal(
        _ndims_from_shape(self._override_event_shape), self._zero))
    self._is_maybe_event_override = bool(
        tensor_util.constant_value(self._override_event_shape) is None or
        tensor_util.constant_value(self._override_event_shape).size != 0)

    # To convert a scalar distribution into a multivariate distribution we
    # will draw dims from the sample dims, which are otherwise iid. This is
    # easy to do except in the case that the base distribution has batch dims
    # and we're overriding event shape. When that case happens the event dims
    # will incorrectly be to the left of the batch dims. In this case we'll
    # cyclically permute left the new dims.
    self._needs_rotation = _logical_and(
        self._is_event_override,
        _logical_not(self._is_batch_override),
        _logical_not(distribution.is_scalar_batch()))
    override_event_ndims = _ndims_from_shape(self._override_event_shape)
    self._rotate_ndims = _pick_scalar_condition(
        self._needs_rotation, override_event_ndims, 0)
    # We'll be reducing the head dims (if at all), i.e., this will be []
    # if we don't need to reduce.
    self._reduce_event_indices = math_ops.range(
        self._rotate_ndims - override_event_ndims, self._rotate_ndims)

self._distribution = distribution
self._bijector = bijector
super(TransformedDistribution, self).__init__(
    dtype=self._distribution.dtype,
    reparameterization_type=self._distribution.reparameterization_type,
    validate_args=validate_args,
    allow_nan_stats=self._distribution.allow_nan_stats,
    parameters=parameters,
    # We let TransformedDistribution access _graph_parents since this class
    # is more like a baseclass than derived.
    graph_parents=(distribution._graph_parents +  # pylint: disable=protected-access
                   bijector.graph_parents),
    name=name)
