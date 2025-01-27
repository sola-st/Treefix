# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Creates a new variable from arguments.

    Args:
      initial_value: A `Tensor`, or Python object convertible to a `Tensor`,
        which is the initial value for the Variable. The initial value must have
        a shape specified unless `validate_shape` is set to False. Can also be a
        callable with no argument that returns the initial value when called.
        (Note that initializer functions from init_ops.py must first be bound to
        a shape before being used here.)
      trainable: If `True`, also adds the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES`. This collection is used as the default
        list of variables to use by the `Optimizer` classes. Defaults to `True`,
        unless `synchronization` is set to `ON_READ`, in which case it defaults
        to `False`.
      collections: List of graph collections keys. The new variable is added to
        these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
      validate_shape: If `False`, allows the variable to be initialized with a
        value of unknown shape. If `True`, the default, the shape of
        `initial_value` must be known.
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
      expected_shape: Deprecated. Ignored.
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
      shape: (optional) The shape of this variable. If None, the shape of
        `initial_value` will be used. When setting this argument to
        `tf.TensorShape(None)` (representing an unspecified shape), the variable
        can be assigned with values of different shapes.

    Raises:
      ValueError: If the initial value is not specified, or does not have a
        shape and `validate_shape` is `True`.
      RuntimeError: If lifted into the eager context.
    """
_ = expected_shape
if initial_value is None:
    raise ValueError("initial_value must be specified.")
init_from_fn = callable(initial_value)

if collections is None:
    collections = [ops.GraphKeys.GLOBAL_VARIABLES]
if not isinstance(collections, (list, tuple, set)):
    raise ValueError(
        "collections argument to Variable constructor must be a list, tuple, "
        "or set. Got %s of type %s" % (collections, type(collections)))
if constraint is not None and not callable(constraint):
    raise ValueError("The `constraint` argument must be a callable.")

# Store the graph key so optimizers know how to only retrieve variables from
# this graph.
self._graph_key = ops.get_default_graph()._graph_key  # pylint: disable=protected-access
if isinstance(initial_value, trackable.CheckpointInitialValue):
    self._maybe_initialize_trackable()
    self._update_uid = initial_value.checkpoint_position.restore_uid
    initial_value = initial_value.wrapped_value

synchronization, aggregation, trainable = (
    validate_synchronization_aggregation_trainable(synchronization,
                                                   aggregation, trainable,
                                                   name))
self._synchronization = synchronization
self._aggregation = aggregation
self._trainable = trainable
if trainable and ops.GraphKeys.TRAINABLE_VARIABLES not in collections:
    collections = list(collections) + [ops.GraphKeys.TRAINABLE_VARIABLES]
with ops.init_scope():
    # Ensure that we weren't lifted into the eager context.
    if context.executing_eagerly():
        raise RuntimeError(
            "Reference variables are not supported when eager execution is "
            "enabled. Please run `tf.compat.v1.enable_resource_variables()` to "
            "switch to resource variables.")
    with ops.name_scope(name, "Variable",
                        [] if init_from_fn else [initial_value]) as name:

        if init_from_fn:
            # Use attr_scope and device(None) to simulate the behavior of
            # colocate_with when the variable we want to colocate with doesn't
            # yet exist.
            true_name = ops.name_from_scope_name(name)  # pylint: disable=protected-access
            attr = attr_value_pb2.AttrValue(
                list=attr_value_pb2.AttrValue.ListValue(
                    s=[compat.as_bytes("loc:@%s" % true_name)]))
            # pylint: disable=protected-access
            with ops.get_default_graph()._attr_scope({"_class": attr}):
                with ops.name_scope("Initializer"), ops.device(None):
                    initial_value = initial_value()
                    if isinstance(initial_value, trackable.CheckpointInitialValue):
                        self._maybe_initialize_trackable()
                        self._update_uid = initial_value.checkpoint_position.restore_uid
                        initial_value = initial_value.wrapped_value
                    self._initial_value = ops.convert_to_tensor(
                        initial_value, name="initial_value", dtype=dtype)
                    if shape is None:
                        shape = (
                            self._initial_value.get_shape()
                            if validate_shape else tensor_shape.unknown_shape())
                self._variable = state_ops.variable_op_v2(
                    shape, self._initial_value.dtype.base_dtype, name=name)
            # pylint: enable=protected-access

        # Or get the initial value from a Tensor or Python object.
        else:
            self._initial_value = ops.convert_to_tensor(
                initial_value, name="initial_value", dtype=dtype)
            # pylint: disable=protected-access
            if self._initial_value.op._get_control_flow_context() is not None:
                raise ValueError(
                    "Initializer for variable %s is from inside a control-flow "
                    "construct, such as a loop or conditional. When creating a "
                    "variable inside a loop or conditional, use a lambda as the "
                    "initializer." % name)
            if shape is None:
                # pylint: enable=protected-access
                shape = (
                    self._initial_value.get_shape()
                    if validate_shape else tensor_shape.unknown_shape())
            # In this case, the variable op can't be created until after the
            # initial_value has been converted to a Tensor with a known type.
            self._variable = state_ops.variable_op_v2(
                shape, self._initial_value.dtype.base_dtype, name=name)

        # Cache the name in `self`, because some APIs call `Variable.name` in a
        # tight loop, and this halves the cost.
        self._name = self._variable.name

        # Manually overrides the variable's shape with the initial value's.
        if validate_shape:
            initial_value_shape = self._initial_value.get_shape()
            if not initial_value_shape.is_fully_defined():
                raise ValueError("initial_value must have a shape specified: %s" %
                                 self._initial_value)

        # If 'initial_value' makes use of other variables, make sure we don't
        # have an issue if these other variables aren't initialized first by
        # using their initialized_value() method.
        self._initializer_op = state_ops.assign(
            self._variable,
            _try_guard_against_uninitialized_dependencies(
                name, self._initial_value),
            validate_shape=validate_shape).op

        # TODO(vrv): Change this class to not take caching_device, but
        # to take the op to colocate the snapshot with, so we can use
        # colocation rather than devices.
        if caching_device is not None:
            with ops.device(caching_device):
                self._snapshot = array_ops.identity(self._variable, name="read")
        else:
            with ops.colocate_with(self._variable.op):
                self._snapshot = array_ops.identity(self._variable, name="read")
    ops.add_to_collections(collections, self)

self._caching_device = caching_device
self._save_slice_info = None
self._constraint = constraint
