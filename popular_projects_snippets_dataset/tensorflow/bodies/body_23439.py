# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
self._check_external_modification()

if isinstance(key, slice):
    # Note: this is quite inefficient, but the list API supports a broad range
    # of slice setters (e.g. truncate, extend, replace) and imitating this
    # for a range of Python versions is non-trivial.
    storage_copy = list(self._storage)
    self._storage[key] = value

    len_before = len(storage_copy)
    len_now = len(self._storage)
    for i in range(max(len_before, len_now)):
        value_now = self._storage[i] if i < len_now else None
        value_before = storage_copy[i] if i < len_before else None

        if isinstance(value_before, base.Trackable):
            self._non_append_mutation = True

        if value_now is not None and value_now != value_before:
            self._storage[i] = self._track_value(self._storage[i],
                                                 self._name_element(i))

else:
    if isinstance(self._storage[key], base.Trackable):
        self._non_append_mutation = True
    self._storage[key] = self._track_value(value, self._name_element(key))

self._update_snapshot()
