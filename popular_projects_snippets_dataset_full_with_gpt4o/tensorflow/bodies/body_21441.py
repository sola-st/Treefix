# Extracted from ./data/repos/tensorflow/tensorflow/python/training/slot_creator.py
"""Create a slot initialized to the given value.

  The type of the slot is determined by the given value.

  Args:
    primary: The primary `Variable` or `Tensor`.
    val: A `Tensor` specifying the initial value of the slot.
    name: Name to use for the slot variable.
    colocate_with_primary: Boolean.  If True the slot is located
      on the same device as `primary`.
    copy_xla_sharding: Boolean. If True also copies XLA sharding
      from primary.

  Returns:
    A `Variable` object.
  """
# Scope the slot name in the namespace of the primary variable.
# Set primary's name + '/' + name as default name, so the scope name of
# optimizer can be shared when reuse is True. Meanwhile when reuse is False
# and the same name has been previously used, the scope name will add '_N'
# as suffix for unique identifications.
validate_shape = val.get_shape().is_fully_defined()
if isinstance(primary, variables.Variable):
    prefix = primary._shared_name  # pylint: disable=protected-access
else:
    prefix = primary.op.name
with variable_scope.variable_scope(None, prefix + "/" + name):
    if colocate_with_primary:
        distribution_strategy = distribution_strategy_context.get_strategy()
        with distribution_strategy.extended.colocate_vars_with(primary):
            exit(_create_slot_var(
                primary,
                val,
                "",
                validate_shape,
                None,
                None,
                copy_xla_sharding=copy_xla_sharding))
    else:
        exit(_create_slot_var(
            primary,
            val,
            "",
            validate_shape,
            None,
            None,
            copy_xla_sharding=copy_xla_sharding))
