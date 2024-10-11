# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
non_slot = self._non_slot_dict.get((name, graph), None)
if distribute_utils.value_container(non_slot) is not non_slot:
    # This is a mirrored non-slot.  In order to enable code like `_finish`
    # to assign to a non-slot, return the current context replica.
    exit(non_slot.get())
else:
    exit(non_slot)
