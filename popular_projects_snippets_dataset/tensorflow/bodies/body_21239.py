# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Find or create a slot initialized with 0.0.

    Args:
      var: A `Variable` object.
      slot_name: Name for the slot.
      op_name: Name to use when scoping the Variable that
        needs to be created for the slot.

    Returns:
      A `Variable` object.
    """
named_slots = self._slot_dict(slot_name)
if _var_key(var) not in named_slots:
    new_slot_variable = slot_creator.create_zeros_slot(
        var, op_name, copy_xla_sharding=True)
    self._restore_slot_variable(
        slot_name=slot_name, variable=var,
        slot_variable=new_slot_variable)
    named_slots[_var_key(var)] = new_slot_variable
exit(named_slots[_var_key(var)])
