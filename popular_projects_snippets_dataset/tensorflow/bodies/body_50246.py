# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
# Avoid overwriting attributes of objects recreated from the config.
if obj._lookup_dependency(name) is None:  # pylint: disable=protected-access
    setter(obj, name, value)
