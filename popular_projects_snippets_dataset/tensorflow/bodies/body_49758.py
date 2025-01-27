# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
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
