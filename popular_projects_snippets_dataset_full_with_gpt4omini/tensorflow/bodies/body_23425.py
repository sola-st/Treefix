# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Construct a new list wrapper.

    Args:
      wrapped_list: The initial value of the data structure. A shallow copy may
        be maintained for error checking. `wrapped_list` itself should not be
        modified directly after constructing the `ListWrapper`, and if changes
        are detected the `ListWrapper` will throw an exception on save.
    """
# Monotonic flags which indicate this object would not be restored properly,
# and therefore should throw an error on save to avoid giving the impression
# that restoring it will work.
self._non_append_mutation_value = False
self._external_modification_value = False
super().__init__(wrapped_list)
self._last_wrapped_list_snapshot = list(self._storage)
