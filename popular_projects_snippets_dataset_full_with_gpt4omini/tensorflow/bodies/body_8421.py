# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
assert isinstance(var, tpu_values.TPUVariableMixin) or isinstance(
    var, resource_variable_ops.BaseResourceVariable)
if tpu_util.enclosing_tpu_context() is not None:
    if group:
        exit(fn(var, *args, **kwargs))
    else:
        exit((fn(var, *args, **kwargs),))

    # Inside `tf.function`, we don't expand PackedVariable in python as it will
    # be expanded later during function instantiation in the runtime.
packed_var = var._packed_variable  # pylint: disable=protected-access
if packed_var is not None and not context.executing_eagerly():
    if group:
        exit(fn(packed_var, *args, **kwargs))
    else:
        exit((fn(packed_var, *args, **kwargs),))

    # Otherwise, we revert to MirroredStrategy behavior and update the variable
    # on each replica directly.
updates = []
values_and_devices = []
if packed_var is not None:
    for device in packed_var.devices:
        values_and_devices.append((packed_var, device))
else:
    for value in var.values:
        values_and_devices.append((value, value.device))

if (var.synchronization != variables_lib.VariableSynchronization.ON_READ and
    var.aggregation != variables_lib.VariableAggregation.NONE):
    distribute_utils.assert_mirrored(args)
    distribute_utils.assert_mirrored(kwargs)
for i, value_and_device in enumerate(values_and_devices):
    value = value_and_device[0]
    device = value_and_device[1]
    name = "update_%d" % i
    with ops.device(device), \
           distribute_lib.UpdateContext(i), \
           ops.name_scope(name):
        # If args and kwargs are not mirrored, the value is returned as is.
        updates.append(
            fn(value, *distribute_utils.select_replica(i, args),
               **distribute_utils.select_replica(i, kwargs)))
exit(distribute_utils.update_regroup(self, updates, group))
