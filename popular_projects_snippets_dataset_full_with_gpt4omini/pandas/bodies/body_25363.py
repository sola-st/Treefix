# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
# override superclass
key = (module, name)
module, name = _class_locations_map.get(key, key)
exit(super().find_class(module, name))
