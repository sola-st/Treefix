# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
"""Packs a list of variables which are distributed across devices.

    Args:
      distributed_variables: A list of distributed Variables to pack.
      name: Optional name for the variable. Defaults to `'Variable'` and gets
        uniquified automatically.
    """
if not ops.executing_eagerly_outside_functions():
    raise ValueError(
        "PackedDistributedVariable should be created in eager mode.")
if not distributed_variables:
    raise ValueError("Expect a non-empty list of variables to pack.")
for i, var in enumerate(distributed_variables):
    if not resource_variable_ops.is_resource_variable(var):
        raise ValueError("Expect a list of ResourceVariables to pack, "
                         "but the %d-th variable is %s" % (i, type(var)))

self._distributed_variables = distributed_variables
self._devices = [v.device for v in distributed_variables]
with ops.init_scope():
    with ops.name_scope(name, "Variable", skip_on_eager=False) as name:
        handle = ops.pack_eager_tensors(
            [var.handle for var in distributed_variables])
        handle_name = ops.name_from_scope_name(name)
        unique_id = "%s_%d" % (handle_name, ops.uid())
        super(PackedDistributedVariable, self).__init__(
            trainable=distributed_variables[0].trainable,
            shape=distributed_variables[0].shape,
            dtype=distributed_variables[0].dtype,
            handle=handle,
            synchronization=distributed_variables[0].synchronization,
            constraint=distributed_variables[0].constraint,
            aggregation=distributed_variables[0].aggregation,
            distribute_strategy=distributed_variables[0]._distribute_strategy,  # pylint: disable=protected-access
            name=name,
            unique_id=unique_id,
            handle_name=handle_name,
            graph_element=None,
            initial_value=None,
            initializer_op=None,
            is_initialized_op=None,
            cached_value=None,
            caching_device=None,
            is_distributed_variables=True)
