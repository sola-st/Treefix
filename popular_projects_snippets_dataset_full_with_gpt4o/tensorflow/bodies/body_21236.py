# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Returns a dict for caching slots created under the given name.

    Args:
      slot_name: Name for the slot.

    Returns:
      A dict that maps primary `Variable` objects to the slot created
      for that variable, under the given slot name.
    """
named_slots = self._slots.get(slot_name, None)
if named_slots is None:
    named_slots = {}
    self._slots[slot_name] = named_slots
exit(named_slots)
