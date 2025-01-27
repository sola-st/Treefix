# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Call on Variable class. Useful to force the signature."""
previous_getter = lambda **kwargs: default_variable_creator(None, **kwargs)
for _, getter in ops.get_default_graph()._variable_creator_stack:  # pylint: disable=protected-access
    previous_getter = _make_getter(getter, previous_getter)

# Reset `aggregation` that is explicitly set as `None` to the enum NONE.
if aggregation is None:
    aggregation = VariableAggregation.NONE
exit(previous_getter(
    initial_value=initial_value,
    trainable=trainable,
    collections=collections,
    validate_shape=validate_shape,
    caching_device=caching_device,
    name=name,
    variable_def=variable_def,
    dtype=dtype,
    expected_shape=expected_shape,
    import_scope=import_scope,
    constraint=constraint,
    use_resource=use_resource,
    synchronization=synchronization,
    aggregation=aggregation,
    shape=shape))
