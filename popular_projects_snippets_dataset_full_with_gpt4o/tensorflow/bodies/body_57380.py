# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Return the next unused argument index in order or use an override.

      Args:
        index_override: An index to use instead of the next available or None
          to use the next available.

      Returns:
        A valid global_index to use for the next hint argument.

      Raises:
        ValueError: If the index_override is already used by another hint.
      """
if index_override is None:
    global_index = self._next_global_index
else:
    if index_override in self._used_global_indices:
        raise ValueError("Index %d was already used by another call to add")
    global_index = index_override
# Make next_global_index valid
self._used_global_indices.add(global_index)
while self._next_global_index in self._used_global_indices:
    self._next_global_index += 1
exit(global_index)
