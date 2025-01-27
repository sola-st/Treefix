# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Creates a variable.

    Args:
      initial_value: A `Tensor`, or Python object convertible to a `Tensor`,
        which is the initial value for the Variable. The initial value must have
        a shape specified unless `validate_shape` is set to False. Can also be a
        callable with no argument that returns the initial value when called.
        (Note that initializer functions from init_ops.py must first be bound
         to a shape before being used here.)
      trainable: If `True`, GradientTapes automatically watch uses of this
        Variable.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      name: Optional name for the variable. Defaults to `'Variable'` and gets
        uniquified automatically.
      dtype: If set, initial_value will be converted to the given type.
        If None, either the datatype will be kept (if initial_value is
       a Tensor) or float32 will be used (if it is a Python object convertible
       to a Tensor).
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value
        (which must have the same shape). Constraints are not safe to
        use when doing asynchronous distributed training.
      add_initializers_to: if not None and not in legacy graph mode, the
        initializer tensor will be added to this map in addition to adding the
        assignment to the function.
      lifted_initializer_graph: FuncGraph to try to lift initializers to.
      synchronization: Indicates when a distributed variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses
        when to synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      shape: (optional) The shape of this variable. If None, the shape of
        `initial_value` will be used. When setting this argument to
        `tf.TensorShape(None)` (representing an unspecified shape), the variable
        can be assigned with values of different shapes.

    Raises:
      ValueError: If the initial value is not specified, or does not have a
        shape and `validate_shape` is `True`.
      RuntimeError: If called outside of a function definition.
    """
with ops.init_scope():
    self._in_graph_mode = not context.executing_eagerly()
if not ops.inside_function():
    # If we've been init_scope()d out of the function definition nothing to do
    # here; we can't really do the capturing or conditional logic.
    resource_variable_ops.ResourceVariable.__init__(
        self, initial_value=initial_value, trainable=trainable,
        caching_device=caching_device, name=name, dtype=dtype,
        constraint=constraint)
    exit()
if initial_value is None:
    raise ValueError("`initial_value` must be a Tensor or a Python "
                     "object convertible to a Tensor. Got None.")
init_from_fn = callable(initial_value)

if constraint is not None and not callable(constraint):
    raise ValueError(f"`constraint` with type {type(constraint)} must be a "
                     "callable.")

with ops.name_scope(name, "Variable", []
                    if init_from_fn else [initial_value]) as scope_name:
    with ops.name_scope("Initializer"):
        if init_from_fn:
            initial_value = initial_value()
        if isinstance(initial_value, trackable.CheckpointInitialValue):
            self._maybe_initialize_trackable()
            self._update_uid = initial_value.checkpoint_position.restore_uid
            initial_value = initial_value.wrapped_value

        initial_value = ops.convert_to_tensor(initial_value,
                                              name="initial_value", dtype=dtype)
    assert initial_value is not None

    # Don't use `shape or initial_value.shape` since TensorShape has
    # overridden `__bool__`.
    if shape is None:
        shape = initial_value.shape

    # Use the constructor for UninitializedVariable to start. Outside the name
    # scope so we don't double up the prefix.
super().__init__(
    trainable=trainable,
    caching_device=caching_device,
    name=name,
    shape=shape,
    dtype=initial_value.dtype,
    constraint=constraint,
    synchronization=synchronization,
    aggregation=aggregation,
    extra_handle_data=initial_value,
    **unused_kwargs)

with ops.name_scope(scope_name):
    if self._in_graph_mode:
        with ops.init_scope():
            outer_graph = ops.get_default_graph()
        func_graph = ops.get_default_graph()
        function_placeholders = (
            func_graph.inputs + func_graph.internal_captures)
        placeholder_ops = set(
            [tensor.op for tensor in function_placeholders])
        lifted_initializer = lift_to_graph.lift_to_graph(
            [initial_value], outer_graph,
            disallowed_placeholders=placeholder_ops)[initial_value]
        with ops.init_scope():
            self._initial_value = lifted_initializer
            with ops.name_scope("IsInitialized"):
                self._is_initialized_op = (
                    resource_variable_ops.var_is_initialized_op(self._handle))
            if initial_value is not None:
                with ops.name_scope("Assign") as n, ops.colocate_with(self._handle):
                    self._initializer_op = resource_variable_ops.assign_variable_op(
                        self._handle, lifted_initializer, name=n)
    elif context.executing_eagerly():
        # In this case, both current scope and init scope are eager.
        # Assign_variable_op will be executed immediately. So we don't need to
        # add it to "add_initializers_to" to lift it out.
        with ops.name_scope("Assign") as n, ops.colocate_with(self._handle):
            resource_variable_ops.assign_variable_op(
                self._handle, initial_value, name=n)
    else:
        # Init scope is eager but current scope is graph. We will lift out this
        # variable by addint it into "add_initializers_to".
        if add_initializers_to is not None:
            add_initializers_to.append((self, initial_value))

        def assign_fn():
            with ops.name_scope("Assign") as n, ops.colocate_with(self._handle):
                resource_variable_ops.assign_variable_op(
                    self._handle,
                    initial_value,
                    name=n)
                # Returning values to keep tf.cond happy.
            exit(ops.convert_to_tensor(1))
        def not_assign_fn():
            exit(ops.convert_to_tensor(0))
        # Note: this cond is always guaranteed to run because we're inside a
        # TracingCompiler which will insert automatic control dependencies.
        # It will only execute assign_fn if lifting failed.
        graph = ops.get_default_graph()

        # Capture the handle ahead of time in order to avoid querying the shape
        # of the handle which helps async execution performance
        graph.capture(self._handle, shape=())
        control_flow_ops.cond(
            resource_variable_ops.var_is_initialized_op(self._handle),
            not_assign_fn, assign_fn)
