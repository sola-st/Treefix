# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
is_scalar = (
    shape is not None and isinstance(shape, collections_abc.Sequence) and
    not shape)
# Partitioned variable case
if partitioner is not None and not is_scalar:
    if not callable(partitioner):
        raise ValueError("Partitioner must be callable, but received: %s" %
                         partitioner)
    with ops.name_scope(None):
        exit(self._get_partitioned_variable(
            name=name,
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

      # Special case for partitioned variable to allow reuse without having to
      # specify partitioner.
if (reuse is True and partitioner is None
    and name in self._partitioned_vars):
    exit(self._get_partitioned_variable(
        name=name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        regularizer=regularizer,
        reuse=reuse,
        trainable=trainable,
        collections=collections,
        caching_device=caching_device,
        partitioner=None,
        validate_shape=validate_shape,
        use_resource=use_resource,
        constraint=constraint,
        synchronization=synchronization,
        aggregation=aggregation))

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
    collections=collections,
    caching_device=caching_device,
    validate_shape=validate_shape,
    use_resource=use_resource,
    constraint=constraint,
    synchronization=synchronization,
    aggregation=aggregation))
