# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
name = self._name_element(key)
value = self._track_value(value, name=name)
current_value = self._storage.setdefault(key, value)
if current_value is not value:
    raise ValueError(
        "Mappings are an append-only data structure. Tried to overwrite the "
        f"key '{key}' with value {value}, but it already contains "
        f"{current_value}")
