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

    Set `reuse` to `True` when you only want to reuse existing Variables.
    Set `reuse` to `False` when you only want to create new Variables.
    Set `reuse` to None (the default) or tf.compat.v1.AUTO_REUSE when you want
    variables to be created if they don't exist or returned if they do.

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
      name: the name of the new or existing sharded variable.
      partitioner: Optional callable that accepts a fully defined `TensorShape`
        and `dtype` of the Variable to be created, and returns a list of
        partitions for each axis (currently only one axis can be partitioned).
      shape: shape of the new or existing sharded variable.
      dtype: type of the new or existing sharded variable (defaults to
        `DT_FLOAT`).
      initializer: initializer for the sharded variable.
      regularizer: a (Tensor -> Tensor or None) function; the result of applying
        it on a newly created variable will be added to the collection
        GraphKeys.REGULARIZATION_LOSSES and can be used for regularization.
      reuse: a Boolean, None, or tf.AUTO_REUSE. Controls reuse or creation of
        variables.
      trainable: If `True` also add the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
      collections: List of graph collections keys to add the Variable to.
        Defaults to `[GraphKeys.GLOBAL_VARIABLES]` (see `tf.Variable`).
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the Variable reside, to
        deduplicate copying through `Switch` and other conditional statements.
      validate_shape: If False, allows the variable to be initialized with a
        value of unknown shape. If True, the default, the shape of initial_value
        must be known.
      use_resource: If False, creates a regular Variable. If True, creates an
        experimental ResourceVariable which has well-defined semantics. Defaults
        to False (will later change to True).
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
      A `PartitionedVariable` object.

    Raises:
      ValueError: when creating a new variable and shape is not declared,
        when reusing a variable and specifying a conflicting shape,
        when violating reuse during variable creation, or if an existing
        sharded variable exists for the given name but with different sharding.
    """
initializing_from_value = initializer is not None and isinstance(
    initializer, ops.Tensor)
if name in self._vars:
    raise ValueError(
        "A partitioner was provided, but an unpartitioned version of the "
        "variable was found: %s.  Perhaps a variable of the same name was "
        "already created without partitioning?" % name)

shape = tensor_shape.as_shape(shape)
if initializing_from_value:
    shape = shape.merge_with(initializer.get_shape())

partitions = None
if not reuse or partitioner:
    partitions = _call_partitioner(partitioner, shape, dtype)

if name in self._partitioned_vars:
    if reuse is False:
        raise ValueError(
            "Partitioned variable with name %s already exists. Did you mean to "
            "set reuse=True or reuse=tf.AUTO_REUSE in VarScope?" % name)

    existing_var = self._partitioned_vars[name]
    if not shape.is_compatible_with(existing_var.get_shape()):
        raise ValueError(
            "Trying to reuse partitioned variable %s, but specified shape %s "
            "and found shape %s." % (name, shape, existing_var.get_shape()))
    if not dtype.is_compatible_with(existing_var.dtype):
        raise ValueError(
            "Trying to reuse partitioned variable %s, but specified dtype %s "
            "and found dtype %s." % (name, dtype.name, existing_var.dtype.name))

    # pylint: disable=protected-access
    if (partitions is not None and
        existing_var._get_partitions() != partitions):
        raise ValueError(
            "Trying to reuse partitioned variable %s, but specified partitions "
            "%s and found partitions %s." %
            (name, partitions, existing_var._get_partitions()))
    # pylint: enable=protected-access

    exit(existing_var)

if reuse is True:
    raise ValueError("PartitionedVariable %s does not exist, or was not "
                     "created with tf.get_variable(). Did you mean to set "
                     "reuse=False or reuse=tf.AUTO_REUSE in VarScope?" % name)

slice_dim, num_slices = _get_slice_dim_and_num_slices(partitions)

if "%s/part_0" % name in self._vars:
    if "%s/part_%d" % (name, num_slices - 1) not in self._vars:
        raise ValueError(
            "Partitioner returned a different partitioning than what was "
            "already found.  Partitioner returned %d shards, and shard "
            "%s/part_0 was found, but %s/part_%d was not." %
            (num_slices, name, name, num_slices - 1))
    if "%s/part_%d" % (name, num_slices) in self._vars:
        raise ValueError(
            "Partitioner returned a different partitioning than what was "
            "already found.  Partitioner returned %d shards, and shard "
            "%s/part_0 was found, but so was the extra shard %s/part_%d." %
            (num_slices, name, name, num_slices))

vs = []
for i, (var_offset, var_shape) in enumerate(
    _iter_slices(shape.as_list(), num_slices, slice_dim)):
    partition_info = _PartitionInfo(
        full_shape=shape.as_list(), var_offset=var_offset)
    var_full_name = "%s/part_%d" % (name, i)
    with ops.name_scope(
        var_full_name + "/PartitionedInitializer", skip_on_eager=False):
        # Create the tensor to initialize the variable with default value.
        if initializer is None:
            init, initializing_from_value = self._get_default_initializer(
                name=name, shape=shape, dtype=dtype)
            if initializing_from_value:
                init_shape = None
            else:
                init_shape = var_shape
        elif callable(initializer):
            init = initializer
            init_shape = var_shape
        elif isinstance(initializer, ops.Tensor):
            init = array_ops.slice(initializer, var_offset, var_shape)
            # Use the dtype of the given tensor.
            dtype = init.dtype.base_dtype
            init_shape = None
        else:
            init = ops.convert_to_tensor(initializer, dtype=dtype)
            init = array_ops.slice(init, var_offset, var_shape)
            init_shape = None

    with ops.name_scope(None):
        var = self._get_single_variable(
            name=var_full_name,
            shape=init_shape,
            dtype=dtype,
            initializer=init,
            partition_info=partition_info,
            regularizer=regularizer,
            reuse=reuse,
            trainable=trainable,
            collections=collections,
            caching_device=caching_device,
            validate_shape=validate_shape,
            use_resource=use_resource,
            constraint=constraint,
            synchronization=synchronization,
            aggregation=aggregation)

    # pylint: disable=protected-access
    var._set_save_slice_info(
        variables.Variable.SaveSliceInfo(name, shape.as_list(), var_offset,
                                         var_shape))
    vs.append(var)
    # pylint: enable=protected-access

partitioned_var = variables.PartitionedVariable(
    name=name,
    shape=shape,
    dtype=dtype,
    variable_list=vs,
    partitions=partitions)
if not context.executing_eagerly() or self._store_eager_variables:
    self._partitioned_vars[name] = partitioned_var
exit(partitioned_var)
