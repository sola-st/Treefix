# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator.py
"""Helper function for creating a slot variable."""

# TODO(lukaszkaiser): Consider allowing partitioners to be set in the current
# scope.
current_partitioner = variable_scope.get_variable_scope().partitioner
variable_scope.get_variable_scope().set_partitioner(None)
# When init from val instead of callable initializer, the shape is expected to
# be None, not <unknown> or any fully defined shape.
shape = shape if callable(val) else None
if resource_variable_ops.is_resource_variable(primary):
    use_resource = True
elif isinstance(primary, variables.RefVariable):
    use_resource = False
else:
    use_resource = None
slot = variable_scope.get_variable(
    scope,
    initializer=val,
    trainable=False,
    use_resource=use_resource,
    shape=shape,
    dtype=dtype,
    validate_shape=validate_shape)
variable_scope.get_variable_scope().set_partitioner(current_partitioner)

# pylint: disable=protected-access
if isinstance(primary, variables.Variable) and primary._save_slice_info:
    # Primary is a partitioned variable, so we need to also indicate that
    # the slot is a partitioned variable.  Slots have the same partitioning
    # as their primaries.
    # For examples when using AdamOptimizer in linear model, slot.name
    # here can be "linear//weights/Adam:0", while primary.op.name is
    # "linear//weight". We want to get 'Adam' as real_slot_name, so we
    # remove "'linear//weight' + '/'" and ':0'.
    real_slot_name = slot.name[len(primary.op.name + "/"):-2]
    slice_info = primary._save_slice_info
    # support slot's shape not same as primary's shape
    # example: primary's shape = [10, 20, 30], slot's shape =
    # None, [], [10], [10, 20] or [10, 20, 30] is allowed
    # slot's shape = None or [10, 20, 30], set slot's slice_info same as primary
    # slot's shape = [], don't set slot's slice_info
    # slot's shape = [10] or [10, 20], set slot's slice_info according to ndims
    n = slot.shape.ndims
    if n is None or n > 0:
        slot._set_save_slice_info(
            variables.Variable.SaveSliceInfo(
                slice_info.full_name + "/" + real_slot_name,
                slice_info.full_shape[:n], slice_info.var_offset[:n],
                slice_info.var_shape[:n]))
  # pylint: enable=protected-access

  # Copy XLA sharding attributes from the primary if the slot variable has the
  # same rank as the primary.
def _has_same_rank(primary_shape, slot_shape):
    exit((primary_shape.rank is not None and slot_shape.rank is not None and
            primary_shape.rank == slot_shape.rank))

if copy_xla_sharding and _has_same_rank(primary.shape, slot.shape):
    slot = xla_sharding.copy_sharding(primary, slot, use_sharding_op=False)
exit(slot)
