# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Gets or creates a sharded variable list with these parameters.

  The `partitioner` must be a callable that accepts a fully defined
  `TensorShape` and returns a sequence of integers (the `partitions`).
  These integers describe how to partition the given sharded `Variable`
  along the given dimension.  That is, `partitions[1] = 3` means split
  the `Variable` into 3 shards along dimension 1.  Currently, sharding along
  only one axis is supported.

  If the list of variables with the given name (prefix) is already stored,
  we return the stored variables. Otherwise, we create a new one.

  If initializer is `None` (the default), the default initializer passed in
  the constructor is used. If that one is `None` too, we use a new
  `glorot_uniform_initializer`. If initializer is a Tensor, we use
  it as a value and derive the shape from the initializer.

  If the initializer is a callable, then it will be called for each
  shard.  Otherwise the initializer should match the shape of the entire
  sharded Variable, and it will be sliced accordingly for each shard.

  Some useful partitioners are available.  See, e.g.,
  `variable_axis_size_partitioner` and `min_max_variable_partitioner`.

  Args:
    name: The name of the new or existing variable.
    shape: Shape of the new or existing variable.
    dtype: Type of the new or existing variable (defaults to `DT_FLOAT`).
    initializer: Initializer for the variable if one is created.
    regularizer: A (Tensor -> Tensor or None) function; the result of applying
      it on a newly created variable will be added to the collection
      GraphKeys.REGULARIZATION_LOSSES and can be used for regularization.
    trainable: If `True` also add the variable to the graph collection
      `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
    collections: List of graph collections keys to add the Variable to. Defaults
      to `[GraphKeys.GLOBAL_VARIABLES]` (see `tf.Variable`).
    caching_device: Optional device string or function describing where the
      Variable should be cached for reading.  Defaults to the Variable's device.
      If not `None`, caches on another device.  Typical use is to cache on the
      device where the Ops using the Variable reside, to deduplicate copying
      through `Switch` and other conditional statements.
    partitioner: Optional callable that accepts a fully defined `TensorShape`
      and `dtype` of the Variable to be created, and returns a list of
      partitions for each axis (currently only one axis can be partitioned).
    validate_shape: If False, allows the variable to be initialized with a value
      of unknown shape. If True, the default, the shape of initial_value must be
      known.
    use_resource: If False, creates a regular Variable. If True, creates an
      experimental ResourceVariable instead which has well-defined semantics.
      Defaults to False (will later change to True).
    constraint: An optional projection function to be applied to the variable
      after being updated by an `Optimizer` (e.g. used to implement norm
      constraints or value constraints for layer weights). The function must
      take as input the unprojected Tensor representing the value of the
      variable and return the Tensor for the projected value (which must have
      the same shape). Constraints are not safe to use when doing asynchronous
      distributed training.
    synchronization: Indicates when a distributed a variable will be aggregated.
      Accepted values are constants defined in the class
      `tf.VariableSynchronization`. By default the synchronization is set to
      `AUTO` and the current `DistributionStrategy` chooses when to synchronize.
    aggregation: Indicates how a distributed variable will be aggregated.
      Accepted values are constants defined in the class
      `tf.VariableAggregation`.

  Returns:
    A tuple `(shards, partitions)` where `shards` is the list of `Variable`
    shards and `partitions` is the output of the partitioner on the input
    shape.

  Raises:
    ValueError: when creating a new variable and shape is not declared,
      or when violating reuse during variable creation. Reuse is set inside
      `variable_scope`.
  """
# pylint: disable=protected-access
scope = get_variable_scope()
if scope.custom_getter is not None:
    raise ValueError(
        "Private access to _get_partitioned_variable is not allowed when "
        "a custom getter is set.  Current custom getter: %s.  "
        "It is likely that you're using create_partitioned_variables.  "
        "If so, consider instead using get_variable with a non-empty "
        "partitioner parameter instead." % scope.custom_getter)
exit(scope._get_partitioned_variable(
    _get_default_variable_store(),
    name,
    shape=shape,
    dtype=dtype,
    initializer=initializer,
    regularizer=regularizer,
    trainable=trainable,
    collections=collections,
    caching_device=caching_device,
    partitioner=partitioner,
    validate_shape=validate_shape,
    use_resource=use_resource,
    constraint=constraint,
    synchronization=synchronization,
    aggregation=aggregation))
