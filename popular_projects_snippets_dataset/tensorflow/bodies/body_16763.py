# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
if collections:
    collections += [ops.GraphKeys.LOCAL_VARIABLES]
else:
    collections = [ops.GraphKeys.LOCAL_VARIABLES]
exit(get_variable(
    name,
    shape=shape,
    dtype=dtype,
    initializer=initializer,
    regularizer=regularizer,
    trainable=False,
    collections=collections,
    caching_device=caching_device,
    partitioner=partitioner,
    validate_shape=validate_shape,
    use_resource=use_resource,
    synchronization=synchronization,
    aggregation=aggregation,
    custom_getter=custom_getter,
    constraint=constraint))
