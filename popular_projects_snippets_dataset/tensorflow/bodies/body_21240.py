# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Restore a newly created slot variable's value."""
variable_key = _var_key(variable)
deferred_restorations = self._deferred_slot_restorations.get(
    slot_name, {}).pop(variable_key, [])
# Iterate over restores, highest restore UID first to minimize the number
# of assignments.
deferred_restorations.sort(key=lambda position: position.restore_uid,
                           reverse=True)
for checkpoint_position in deferred_restorations:
    checkpoint_position.restore(slot_variable)
