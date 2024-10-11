# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Adds a new variable to the layer.

    Args:
      name: Variable name.
      shape: Variable shape. Defaults to scalar if unspecified.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      initializer: Initializer instance (callable).
      regularizer: Regularizer instance (callable).
      trainable: Boolean, whether the variable should be part of the layer's
        "trainable_variables" (e.g. variables, biases)
        or "non_trainable_variables" (e.g. BatchNorm mean and variance).
        Note that `trainable` cannot be `True` if `synchronization`
        is set to `ON_READ`.
      constraint: Constraint instance (callable).
      partitioner: Partitioner to be passed to the `Trackable` API.
      use_resource: Whether to use `ResourceVariable`.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses
        when to synchronize. If `synchronization` is set to `ON_READ`,
        `trainable` must not be set to `True`.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      **kwargs: Additional keyword arguments. Accepted values are `getter`,
        `collections`, `experimental_autocast` and `caching_device`.

    Returns:
      The created variable. Usually either a `Variable` or `ResourceVariable`
      instance. If `partitioner` is not `None`, a `PartitionedVariable`
      instance is returned.

    Raises:
      RuntimeError: If called with partitioned variable regularization and
        eager execution is enabled.
      ValueError: When giving unsupported dtype and no initializer or when
        trainable has been set to True with synchronization set as `ON_READ`.
    """
if shape is None:
    shape = ()
# Validate optional keyword arguments.
for kwarg in kwargs:
    if kwarg not in ['getter', 'collections', 'experimental_autocast',
                     'caching_device']:
        raise TypeError('Unknown keyword argument:', kwarg)
has_custom_getter = 'getter' in kwargs
getter = kwargs.pop('getter', base_layer_utils.make_variable)
collections_arg = kwargs.pop('collections', None)
# 'experimental_autocast' can be set to False by the caller to indicate an
# AutoCastVariable should never be created.
autocast = kwargs.pop('experimental_autocast', True)
# See the docstring for tf.Variable about the details for caching_device.
caching_device = kwargs.pop('caching_device', None)

if dtype is None:
    dtype = self.dtype or backend.floatx()
dtype = dtypes.as_dtype(dtype)
if self._dtype_policy.variable_dtype is None:
    # The policy is "_infer", so we infer the policy from the variable dtype.
    self._set_dtype_policy(policy.Policy(dtype.base_dtype.name))
initializer = initializers.get(initializer)
regularizer = regularizers.get(regularizer)
constraint = constraints.get(constraint)

if synchronization == tf_variables.VariableSynchronization.ON_READ:
    if trainable:
        raise ValueError(
            'Synchronization value can be set to '
            'VariableSynchronization.ON_READ only for non-trainable variables. '
            'You have specified trainable=True and '
            'synchronization=VariableSynchronization.ON_READ.')
    else:
        # Set trainable to be false when variable is to be synced on read.
        trainable = False
elif trainable is None:
    trainable = True

# Initialize variable when no initializer provided
if initializer is None:
    # If dtype is DT_FLOAT, provide a uniform unit scaling initializer
    if dtype.is_floating:
        initializer = initializers.get('glorot_uniform')
    # If dtype is DT_INT/DT_UINT, provide a default value `zero`
    # If dtype is DT_BOOL, provide a default value `FALSE`
    elif dtype.is_integer or dtype.is_unsigned or dtype.is_bool:
        initializer = initializers.zeros()
    # NOTES:Do we need to support for handling DT_STRING and DT_COMPLEX here?
    elif not has_custom_getter:
        # When `getter` is specified, it's possibly fine for `initializer` to be
        # None since it's up to the custom `getter` to raise error in case it
        # indeed needs `initializer`.
        raise ValueError('An initializer for variable %s of type %s is required'
                         ' for layer %s' % (name, dtype.base_dtype, self.name))

if (autocast and
    self._dtype_policy.compute_dtype != self._dtype_policy.variable_dtype
    and dtype.is_floating):
    # Wrap 'getter' with a version that returns an AutoCastVariable.
    old_getter = getter
    def getter(*args, **kwargs):  # pylint: disable=function-redefined
        variable = old_getter(*args, **kwargs)
        exit(autocast_variable.create_autocast_variable(variable))
    # Also the caching_device does not work with the mixed precision API,
    # disable it if it is specified.
    # TODO(b/142020079): Reenable it once the bug is fixed.
    if caching_device is not None:
        tf_logging.warning(
            '`caching_device` does not work with mixed precision API. Ignoring '
            'user specified `caching_device`.')
        caching_device = None

variable = self._add_variable_with_custom_getter(
    name=name,
    shape=shape,
    # TODO(allenl): a `make_variable` equivalent should be added as a
    # `Trackable` method.
    getter=getter,
    # Manage errors in Layer rather than Trackable.
    overwrite=True,
    initializer=initializer,
    dtype=dtype,
    constraint=constraint,
    trainable=trainable,
    partitioner=partitioner,
    use_resource=use_resource,
    collections=collections_arg,
    synchronization=synchronization,
    aggregation=aggregation,
    caching_device=caching_device)
if regularizer is not None:
    # TODO(fchollet): in the future, this should be handled at the
    # level of variable creation, and weight regularization losses
    # should be variable attributes.
    name_in_scope = variable.name[:variable.name.find(':')]
    self._handle_weight_regularization(name_in_scope,
                                       variable,
                                       regularizer)
if base_layer_utils.is_split_variable(variable):
    for v in variable:
        backend.track_variable(v)
        if trainable:
            self._trainable_weights.append(v)
        else:
            self._non_trainable_weights.append(v)
else:
    backend.track_variable(variable)
    if trainable:
        self._trainable_weights.append(variable)
    else:
        self._non_trainable_weights.append(variable)
exit(variable)
