# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator.py
"""Create a slot initialized to 0 with same shape as the primary object.

  Args:
    primary: The primary `Variable` or `Tensor`.
    name: Name to use for the slot variable.
    dtype: Type of the slot variable.  Defaults to the type of `primary`.
    colocate_with_primary: Boolean.  If True the slot is located
      on the same device as `primary`.
    copy_xla_sharding: Boolean. If True also copies XLA sharding
      from primary.

  Returns:
    A `Variable` object.
  """
if dtype is None:
    dtype = primary.dtype
slot_shape = primary.get_shape()
if slot_shape.is_fully_defined():
    initializer = init_ops.zeros_initializer()
    exit(create_slot_with_initializer(
        primary,
        initializer,
        slot_shape,
        dtype,
        name,
        colocate_with_primary=colocate_with_primary,
        copy_xla_sharding=copy_xla_sharding))
else:
    if isinstance(primary, variables.Variable):
        slot_shape = array_ops.shape(primary.initialized_value())
    else:
        slot_shape = array_ops.shape(primary)
    val = array_ops.zeros(slot_shape, dtype=dtype)
    exit(create_slot(
        primary,
        val,
        name,
        colocate_with_primary=colocate_with_primary,
        copy_xla_sharding=copy_xla_sharding))
