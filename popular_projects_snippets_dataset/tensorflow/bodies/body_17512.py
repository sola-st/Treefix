# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Creates a variable.

    Args:
      initial_value: A `Tensor`, or Python object convertible to a `Tensor`,
        which is the initial value for the Variable. The initial value must have
        a shape specified unless `validate_shape` is set to False. Can also be a
        callable with no argument that returns the initial value when called.
        (Note that initializer functions from init_ops.py must first be bound to
        a shape before being used here.)
      trainable: If `True`, the default, also adds the variable to the graph
        collection `GraphKeys.TRAINABLE_VARIABLES`. This collection is used as
        the default list of variables to use by the `Optimizer` classes.
        Defaults to `True`, unless `synchronization` is set to `ON_READ`, in
        which case it defaults to `False`.
      collections: List of graph collections keys. The new variable is added to
        these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      name: Optional name for the variable. Defaults to `'Variable'` and gets
        uniquified automatically.
      dtype: If set, initial_value will be converted to the given type. If None,
        either the datatype will be kept (if initial_value is a Tensor) or
        float32 will be used (if it is a Python object convertible to a Tensor).
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
      distribute_strategy: DistributionStrategy under which this variable was
        created.
      shape: (optional) The shape of this variable. If None, the shape of
        `initial_value` will be used. When setting this argument to
        `tf.TensorShape(None)` (representing an unspecified shape), the variable
        can be assigned with values of different shapes.
      validate_shape: If `False`, allows the variable to be initialized with a
        value of unknown shape. If `True`, the default, the shape of
        `initial_value` must be known.
      experimental_enable_variable_lifting: Whether to lift the variable out if
        it's in a `tf.function`. Default is `True`. When this argument
        is `True`, variable creation will follow the behavior and
        restrictions described
        [here](https://www.tensorflow.org/guide/function#creating_tfvariables).
        If this argument is `False`, that description doesn't apply,
        and you can freely create and use the variable in the
        `tf.function`, as if it's a "mutable `tf.Tensor`". You can't
        return the variable though.

    Raises:
      ValueError: If the initial value is not specified, or does not have a
        shape and `validate_shape` is `True`.

    @compatibility(eager)
    When Eager Execution is enabled, variables are never added to collections.
    It is not implicitly added to the `GLOBAL_VARIABLES` or
    `TRAINABLE_VARIABLES` collections, and the `collections` argument is
    ignored.
    @end_compatibility
    """
synchronization, aggregation, trainable = (
    variables.validate_synchronization_aggregation_trainable(
        synchronization, aggregation, trainable, name))
if experimental_enable_variable_lifting is None:
    experimental_enable_variable_lifting = True
if initial_value is None:
    raise ValueError("The `initial_value` arg to `tf.Variable` must "
                     "be specified except when you are not providing a "
                     "`variable_def`. You provided neither.")
init_from_fn = callable(initial_value)

if isinstance(initial_value, ops.Tensor) and hasattr(
    initial_value, "graph") and initial_value.graph.building_function:
    raise ValueError(f"Argument `initial_value` ({initial_value}) could not "
                     "be lifted out of a `tf.function`. "
                     f"(Tried to create variable with name='{name}'). "
                     "To avoid this error, when constructing `tf.Variable`s "
                     "inside of `tf.function` you can create the "
                     "`initial_value` tensor in a "
                     "`tf.init_scope` or pass a callable `initial_value` "
                     "(e.g., `tf.Variable(lambda : "
                     "tf.truncated_normal([10, 40]))`). "
                     "Please file a feature request if this "
                     "restriction inconveniences you.")

if collections is None:
    collections = [ops.GraphKeys.GLOBAL_VARIABLES]
if not isinstance(collections, (list, tuple, set)):
    raise ValueError(
        f"collections argument to Variable constructor must be a list, "
        f"tuple, or set. Got {collections} of type {type(collections)}")
if constraint is not None and not callable(constraint):
    raise ValueError(f"Argument `constraint` must be None or a callable. "
                     f"a callable. Got a {type(constraint)}:  {constraint}")

if trainable and ops.GraphKeys.TRAINABLE_VARIABLES not in collections:
    collections = list(collections) + [ops.GraphKeys.TRAINABLE_VARIABLES]
with ops.init_scope():
    self._in_graph_mode = not context.executing_eagerly()
if experimental_enable_variable_lifting:
    maybe_init_scope = ops.init_scope
else:
    maybe_init_scope = contextlib.nullcontext
with maybe_init_scope():
    with ops.name_scope(
        name,
        "Variable", [] if init_from_fn else [initial_value],
        skip_on_eager=False) as name:
        # pylint: disable=protected-access
        handle_name = ops.name_from_scope_name(name)
        if self._in_graph_mode:
            shared_name = handle_name
            unique_id = shared_name
        else:
            # When in eager mode, use a uid for the shared_name, to prevent
            # accidental sharing.
            unique_id = "%s_%d" % (handle_name, ops.uid())
            shared_name = None  # Never shared
        # Use attr_scope and device(None) to simulate the behavior of
        # colocate_with when the variable we want to colocate with doesn't
        # yet exist.
        device_context_manager = (
            ops.device if self._in_graph_mode else ops.NullContextmanager)
        attr = attr_value_pb2.AttrValue(
            list=attr_value_pb2.AttrValue.ListValue(
                s=[compat.as_bytes("loc:@%s" % handle_name)]))
        with ops.get_default_graph()._attr_scope({"_class": attr}):
            with ops.name_scope("Initializer"), device_context_manager(None):
                if init_from_fn:
                    initial_value = initial_value()
                if isinstance(initial_value, trackable.CheckpointInitialValue):
                    self._maybe_initialize_trackable()
                    self._update_uid = initial_value.checkpoint_position.restore_uid
                    initial_value = initial_value.wrapped_value
                initial_value = ops.convert_to_tensor(
                    initial_value, name="initial_value", dtype=dtype)
            if shape is not None:
                if not initial_value.shape.is_compatible_with(shape):
                    raise ValueError(
                        f"In this `tf.Variable` creation, the initial value's shape "
                        f"({initial_value.shape}) is not compatible with "
                        f"the explicitly supplied `shape` argument ({shape}).")
            else:
                shape = initial_value.shape
            handle = eager_safe_variable_handle(
                initial_value=initial_value,
                shape=shape,
                shared_name=shared_name,
                name=name,
                graph_mode=self._in_graph_mode)
            handle._parent_trackable = weakref.ref(self)
            handle._name = handle_name + ":0"
            handle._unique_id = unique_id
        # pylint: disable=protected-access
        if (self._in_graph_mode and initial_value is not None and
            initial_value.op._get_control_flow_context() is not None):
            raise ValueError(
                f"The `initial_value` passed to `tf.Variable` {name} is from "
                f"inside a control-flow  construct, such as a loop or "
                f"conditional. When creating a "
                f"`tf.Variable` inside a loop or conditional, use a lambda as "
                f"the `initial_value`. Got: initial_value=({initial_value})")
        # pylint: enable=protected-access
        dtype = initial_value.dtype.base_dtype

        if self._in_graph_mode:
            with ops.name_scope("IsInitialized"):
                is_initialized_op = (
                    gen_resource_variable_ops.var_is_initialized_op(handle))
            if initial_value is not None:
                # pylint: disable=g-backslash-continuation
                with ops.name_scope("Assign") as n, \
                 ops.colocate_with(None, ignore_existing=True), \
                 ops.device(handle.device):
                    # pylint: disable=protected-access
                    initializer_op = (
                        gen_resource_variable_ops.assign_variable_op(
                            handle,
                            variables._try_guard_against_uninitialized_dependencies(
                                name, initial_value),
                            name=n))
                    # pylint: enable=protected-access
                # pylint: enable=g-backslash-continuation
            with ops.name_scope("Read"):
                # Manually assign reads to the handle's device to avoid log
                # messages.
                with ops.device(handle.device):
                    value = gen_resource_variable_ops.read_variable_op(handle, dtype)
                    _maybe_set_handle_data(dtype, handle, value)
                graph_element = value
                if caching_device is not None:
                    # Variables may be created in a tf.device() or ops.colocate_with()
                    # context. At the same time, users would expect caching device to
                    # be independent of this context, and/or would not expect the
                    # current device context to be merged with the caching device
                    # spec.  Therefore we reset the colocation stack before creating
                    # the cached value. Note that resetting the colocation stack will
                    # also reset the device stack.
                    with ops.colocate_with(None, ignore_existing=True):
                        with ops.device(caching_device):
                            cached_value = array_ops.identity(value)
                else:
                    cached_value = None
        else:
            gen_resource_variable_ops.assign_variable_op(handle, initial_value)
            is_initialized_op = None
            initializer_op = None
            graph_element = None
            if caching_device:
                with ops.device(caching_device):
                    cached_value = gen_resource_variable_ops.read_variable_op(
                        handle, dtype)
                    _maybe_set_handle_data(dtype, handle, cached_value)
            else:
                cached_value = None

        if cached_value is not None:
            # Store the variable object so that the original variable can be
            # accessed to generate functions that are compatible with SavedModel.
            cached_value._cached_variable = weakref.ref(self)  # pylint: disable=protected-access

        if self._in_graph_mode:
            # Eager variables are only added to collections if they are part of an
            # eager variable store (otherwise in an interactive session they would
            # hog memory and cause OOM). This is done in ops/variable_scope.py.
            ops.add_to_collections(collections, self)
        elif ops.GraphKeys.GLOBAL_STEP in collections:
            ops.add_to_collections(ops.GraphKeys.GLOBAL_STEP, self)
    initial_value = initial_value if self._in_graph_mode else None
    super(ResourceVariable, self).__init__(
        trainable=trainable,
        shape=shape,
        dtype=dtype,
        handle=handle,
        synchronization=synchronization,
        constraint=constraint,
        aggregation=aggregation,
        distribute_strategy=distribute_strategy,
        name=name,
        unique_id=unique_id,
        handle_name=handle_name,
        graph_element=graph_element,
        initial_value=initial_value,
        initializer_op=initializer_op,
        is_initialized_op=is_initialized_op,
        cached_value=cached_value,
        caching_device=caching_device,
        validate_shape=validate_shape,
    )
