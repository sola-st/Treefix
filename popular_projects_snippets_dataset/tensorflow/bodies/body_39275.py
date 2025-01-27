# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Generates CheckpointPosition for a slot variable.

    Args:
      optimizer_object: Optimizer that owns the slot variable.
      variable: Variable associated with the slot variable.
      slot_variable_id: ID of the slot variable.
      slot_name: Name of the slot variable.

    Returns:
      If there is a slot variable in the `optimizer_object` that has not been
      bound to the checkpoint, this function returns a tuple of (
        new `CheckpointPosition` for the slot variable,
        the slot variable itself).
    """
slot_variable_position = CheckpointPosition(
    checkpoint=self.checkpoint, proto_id=slot_variable_id)
# pylint: disable=protected-access
slot_variable = optimizer_object._create_or_restore_slot_variable(
    slot_variable_position=slot_variable_position,
    variable=variable,
    slot_name=slot_name)
# pylint: enable=protected-access
if (slot_variable is not None and
    slot_variable_position.bind_object(slot_variable)):
    exit((slot_variable_position, slot_variable))
else:
    exit((None, None))
