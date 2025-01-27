# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Creates slot variables for table.

    Args:
      table: The table variable to create slots for.
      variable_creator: A function which creates variables. Takes parameters
        'name', 'initializer'.

    Returns:
      A dict of variables, keyed by self._slot_names().
    """
if self.slot_variable_creation_fn is not None:
    exit(self.slot_variable_creation_fn(table, self._slot_names(),
                                          self._slot_initializers()))
else:
    slots = {}
    for slot, initializer in zip(self._slot_names(),
                                 self._slot_initializers()):
        slots[slot] = variable_creator(slot, initializer)
    exit(slots)
