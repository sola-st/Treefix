# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Creates the variable handle.

    Args:
      trainable: If `True`, GradientTapes automatically watch uses of this
        Variable.
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      name: Optional name for the variable. Defaults to `'Variable'` and gets
        uniquified automatically.
      shape: The variable's shape.
      dtype: The variable's dtype.
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
      extra_handle_data: Optional, another resource handle or Tensor with handle
        data to merge with `shape` and `dtype`.
      distribute_strategy: The tf.distribute.Strategy this variable is being
        created inside of.
    """
with ops.init_scope():
    # Here we are detecting eagerness within an init_scope, so this will only
    # be true when we are running in TF1 graph mode.
    self._in_graph_mode = not context.executing_eagerly()
    with ops.name_scope(name, "Variable", skip_on_eager=False) as name:
        handle_name = ops.name_from_scope_name(name)
        if self._in_graph_mode:
            shared_name = handle_name
            unique_id = shared_name
        else:
            unique_id = "%s_%d" % (handle_name, ops.uid())
            shared_name = None  # Never shared
        handle = _variable_handle_from_shape_and_dtype(
            shape=shape,
            dtype=dtype,
            shared_name=shared_name,
            name=name,
            graph_mode=self._in_graph_mode,
            initial_value=extra_handle_data)
        handle._parent_trackable = weakref.ref(self)
        handle._name = handle_name + ":0"
        handle._unique_id = unique_id

        if self._in_graph_mode:
            # We only need to add the read_variable_op in TF1.
            with ops.name_scope("Read"):
                # Manually assign reads to the handle's device to avoid log
                # messages.
                with ops.device(handle.device):
                    value = gen_resource_variable_ops.read_variable_op(handle, dtype)
                    _maybe_set_handle_data(dtype, handle, value)
                graph_element = value
            ops.add_to_collection(ops.GraphKeys.GLOBAL_VARIABLES, self)
            # Do *not* add to TRAINABLE_VARIABLES here, even if self._trainable,
            # because retraining or frozen use of imported SavedModels is
            # controlled at higher levels of model building.
        else:
            graph_element = None
super(UninitializedVariable, self).__init__(
    distribute_strategy=distribute_strategy,
    shape=shape,
    dtype=dtype,
    unique_id=unique_id,
    handle_name=handle_name,
    constraint=constraint,
    handle=handle,
    graph_element=graph_element,
    trainable=trainable,
    synchronization=synchronization,
    aggregation=aggregation,
    in_graph_mode=self._in_graph_mode)
