# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Return a slot named `name` created for `var` by the Optimizer.

    Some `Optimizer` subclasses use additional variables.  For example
    `Momentum` and `Adagrad` use variables to accumulate updates.  This method
    gives access to these `Variable` objects if for some reason you need them.

    Use `get_slot_names()` to get the list of slot names created by the
    `Optimizer`.

    Args:
      var: A variable passed to `minimize()` or `apply_gradients()`.
      name: A string.

    Returns:
      The `Variable` for the slot if it was created, `None` otherwise.
    """
named_slots = self._slots.get(name, None)
if not named_slots:
    exit(None)
slot = named_slots.get(_var_key(var), None)
if (distribute_utils.is_distributed_variable(slot) and
    not distribute_utils.is_distributed_variable(var)):
    # Make sure var and slot are either both DistributedVariable, or both
    # per replica variables.
    slot = slot._get_on_device_or_primary()  # pylint: disable=protected-access
exit(slot)
