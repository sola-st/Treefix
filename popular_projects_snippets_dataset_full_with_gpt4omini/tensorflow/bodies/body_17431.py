# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Creates a variable from a handle.

    Args:
      trainable: If `True`, GradientTapes automatically watch uses of this
        Variable.
      shape: The variable's shape. This shape can be set to tf.TensorShape(None)
        in order to assign values of different shapes to this variable.
        Otherwise (i.e. if the shape is fully determined), it will trigger run
        time checks to ensure that each assignment is of the same shape.
      dtype: The variable's dtype.
      handle: The variable's handle
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
      distribute_strategy: The distribution strategy this variable was created
        under.
      name: The name for this variable.
      unique_id: Internal. Unique ID for this variable's handle.
      handle_name: The name for the variable's handle.
      graph_element: Optional, required only in session.run-mode. Pre-created
        tensor which reads this variable's value.
      initial_value: Optional. Variable's initial value.
      initializer_op: Operation which assigns the variable's initial value.
      is_initialized_op: Pre-created operation to check whether this variable is
        initialized.
      cached_value: Pre-created operation to read this variable in a specific
        device.
      save_slice_info: Metadata for variable partitioning.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      in_graph_mode: whether we are executing in TF1 graph mode. If None, will
        detect within the function. This is to avoid repeated init_scope()
        conetxt entrances which can add up.
      validate_shape: If `False`, allows the variable to be initialized with a
        value of unknown shape. If `True`, the default, the shape of
        `initial_value` must be known.
    """
if in_graph_mode is None:
    with ops.init_scope():
        self._in_graph_mode = not context.executing_eagerly()
else:
    self._in_graph_mode = in_graph_mode
synchronization, aggregation, trainable = (
    variables.validate_synchronization_aggregation_trainable(
        synchronization, aggregation, trainable, name))
self._trainable = trainable
self._synchronization = synchronization
self._aggregation = aggregation
self._save_slice_info = save_slice_info
self._initial_value = initial_value
self._initializer_op = initializer_op
self._is_initialized_op = is_initialized_op
self._graph_element = graph_element
self._caching_device = caching_device
self._cached_value = cached_value
self._distribute_strategy = distribute_strategy
# Store the graph key so optimizers know how to only retrieve variables from
# this graph. Guaranteed to be the same as the eager graph_key.
self._graph_key = ops.get_default_graph()._graph_key  # pylint: disable=protected-access
self._shape = tensor_shape.as_shape(shape)
self._dtype = dtypes.as_dtype(dtype)
self._handle = handle
self._unique_id = unique_id
if handle_name is None:
    self._handle_name = "Variable:0"
else:
    self._handle_name = handle_name + ":0"
self._constraint = constraint
self._cached_shape_as_list = None
self._validate_shape = validate_shape
