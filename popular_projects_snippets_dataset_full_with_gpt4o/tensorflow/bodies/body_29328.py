# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options.py
if not isinstance(value, ty):
    raise TypeError(
        "Property \"{}\" must be of type {}, got: {} (type: {})".format(
            name, ty, value, type(value)))
option._options[name] = value  # pylint: disable=protected-access
