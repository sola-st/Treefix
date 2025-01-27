# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
"""Gets an existing variable with these parameters or create a new one.

    If a variable with the given name is already stored, we return the stored
    variable. Otherwise, we create a new one.

    Set `reuse` to `True` when you only want to reuse existing Variables.
    Set `reuse` to `False` when you only want to create new Variables.
    Set `reuse` to None (the default) or tf.compat.v1.AUTO_REUSE when you want
    variables to be created if they don't exist or returned if they do.

    If initializer is `None` (the default), the default initializer passed in
    the constructor is used. If that one is `None` too, we use a new
    `glorot_uniform_initializer`. If initializer is a Tensor, we use
    it as a value and derive the shape from the initializer.

    If a partitioner is provided, a `PartitionedVariable` is returned.
    Accessing this object as a `Tensor` returns the shards concatenated along
    the partition axis.

    Some useful partitioners are available.  See, e.g.,
    `variable_axis_size_partitioner` and `min_max_variable_partitioner`.

    Args:
      name: The name of the new or existing variable.
      shape: Shape of the new or existing variable.
      dtype: Type of the new or existing variable (defaults to `DT_FLOAT`).
      initializer: Initializer for the variable.
      regularizer: A (Tensor -> Tensor or None) function; the result of applying
        it on a newly created variable will be added to the collection
        GraphKeys.REGULARIZATION_LOSSES and can be used for regularization.
      reuse: a Boolean, None, or tf.AUTO_REUSE. Controls reuse or creation of
        variables. When eager execution is enabled  this argument is always
        forced to be False.
      trainable: If `True` also add the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`). `trainable`
        defaults to `True`, unless `synchronization` is set to `ON_READ`, in
        which case it defaults to `False`.
      collections: List of graph collections keys to add the `Variable` to.
        Defaults to `[GraphKeys.GLOBAL_VARIABLES]` (see `tf.Variable`).
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the `Variable` reside, to
        deduplicate copying through `Switch` and other conditional statements.
      partitioner: Optional callable that accepts a fully defined `TensorShape`
        and dtype of the `Variable` to be created, and returns a list of
        partitions for each axis (currently only one axis can be partitioned).
      validate_shape: If False, allows the variable to be initialized with a
        value of unknown shape. If True, the default, the shape of initial_value
        must be known.
      use_resource: If False, creates a regular Variable. If True, creates
        instead an experimental ResourceVariable which has well-defined
        semantics. Defaults to False (will later change to True). When eager
        execution is enabled this argument is always forced to be true.
      custom_getter: Callable that takes as a first argument the true getter,
        and allows overwriting the internal get_variable method. The signature
        of `custom_getter` should match that of this method,
        but the most future-proof version will allow for changes: `def
          custom_getter(getter, *args, **kwargs)`.  Direct access to
        all `get_variable` parameters is also allowed: `def
          custom_getter(getter, name, *args, **kwargs)`.  A simple identity
        custom getter that simply creates variables with modified names is:
          ```python
        def custom_getter(getter, name, *args, **kwargs): return getter(name +
          '_suffix', *args, **kwargs) ```
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses when to
        synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.

    Returns:
      The created or existing `Variable` (or `PartitionedVariable`, if a
      partitioner was used).

    Raises:
      ValueError: when creating a new variable and shape is not declared,
        when reusing a variable and specifying a conflicting shape,
        or when violating reuse during variable creation.
      RuntimeError: when eager execution is enabled and not called from an
        EagerVariableStore.
    """
if custom_getter is not None and not callable(custom_getter):
    raise ValueError("Passed a custom_getter which is not callable: %s" %
                     custom_getter)

with ops.init_scope():
    if context.executing_eagerly():
        # Variable creation and initialization takes place in `init_scope`s;
        # as such, if an `init_scope` lifts us into the eager context, then we
        # need to use `ResourceVariable`s.
        use_resource = True

    # Note that it's fine to reuse eager variables whose initialization was
    # lifted from a function-building graph into the eager context (that's why
    # the following clause is not wrapped in an `init_scope`); lifted variables
    # are tracked by the graph's `VariableStore`.
if context.executing_eagerly():
    reuse = vs.AUTO_REUSE

# If a *_ref type is passed in an error would be triggered further down the
# stack. We prevent this using base_dtype to get a non-ref version of the
# type, before doing anything else. When _ref types are removed in favor of
# resources, this line can be removed.
try:
    dtype = dtype.base_dtype
except AttributeError:
    # .base_dtype not existing means that we will try and use the raw dtype
    # which was passed in - this might be a NumPy type which is valid.
    pass

# This is the main logic of get_variable.  However, custom_getter
# may override this logic.  So we save it as a callable and pass
# it to custom_getter.
# Note: the parameters of _true_getter, and their documentation, match
# *exactly* item-for-item with the docstring of this method.
def _true_getter(  # pylint: disable=missing-docstring
    name,
    shape=None,
    dtype=dtypes.float32,
    initializer=None,
    regularizer=None,
    reuse=None,
    trainable=None,
    collections=None,  # pylint: disable=unused-argument
    caching_device=None,
    partitioner=None,
    validate_shape=True,
    use_resource=None,  # pylint: disable=unused-argument
    constraint=None,
    synchronization=vs.VariableSynchronization.AUTO,
    aggregation=vs.VariableAggregation.NONE):
    # Partitioned variable currently unsupported w/ the shim
    if partitioner is not None:
        raise ValueError(
            "`partitioner` arg for `get_variable` is unsupported in TF2."
            "File a bug if you need help. You passed %s" % partitioner)

    # Single variable case
    if "%s/part_0" % name in self._vars:
        raise ValueError(
            "No partitioner was provided, but a partitioned version of the "
            "variable was found: %s/part_0. Perhaps a variable of the same "
            "name was already created with partitioning?" % name)

    exit(self._get_single_variable(
        name=name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        regularizer=regularizer,
        reuse=reuse,
        trainable=trainable,
        caching_device=caching_device,
        validate_shape=validate_shape,
        constraint=constraint,
        synchronization=synchronization,
        aggregation=aggregation))

synchronization, aggregation, trainable = (
    validate_synchronization_aggregation_trainable(
        synchronization, aggregation, trainable, name))

if custom_getter is not None:
    # Handle backwards compatibility with getter arguments that were added
    # to the API after users started writing custom getters.
    custom_getter_kwargs = {
        "getter": _true_getter,
        "name": name,
        "shape": shape,
        "dtype": dtype,
        "initializer": initializer,
        "regularizer": regularizer,
        "reuse": reuse,
        "trainable": trainable,
        "collections": collections,
        "caching_device": caching_device,
        "partitioner": partitioner,
        "validate_shape": validate_shape,
        "use_resource": use_resource,
        "synchronization": synchronization,
        "aggregation": aggregation,
    }
    # `fn_args` and `has_kwargs` can handle functions, `functools.partial`,
    # `lambda`.
    if ("constraint" in fn_args(custom_getter) or
        _has_kwargs(custom_getter)):
        custom_getter_kwargs["constraint"] = constraint
    exit(custom_getter(**custom_getter_kwargs))
else:
    exit(_true_getter(
        name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        regularizer=regularizer,
        reuse=reuse,
        trainable=trainable,
        collections=collections,
        caching_device=caching_device,
        partitioner=partitioner,
        validate_shape=validate_shape,
        use_resource=use_resource,
        constraint=constraint,
        synchronization=synchronization,
        aggregation=aggregation))
