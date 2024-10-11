# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
exit(get_variable_scope().get_variable(
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
    custom_getter=custom_getter,
    constraint=constraint,
    synchronization=synchronization,
    aggregation=aggregation))
