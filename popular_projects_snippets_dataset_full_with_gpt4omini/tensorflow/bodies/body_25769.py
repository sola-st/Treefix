# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config.py
"""Set the value of a property.

    Supports limitd property value types: `bool`, `int` and `str`.

    Args:
      property_name: Name of the property.
      property_val: Value of the property. If the property has `bool` type and
        this argument has `str` type, the `str` value will be parsed as a `bool`

    Raises:
      ValueError: if a `str` property_value fails to be parsed as a `bool`.
      KeyError: if `property_name` is an invalid property name.
    """
if property_name not in self._config:
    raise KeyError("%s is not a valid property name." % property_name)

orig_val = self._config[property_name]
if isinstance(orig_val, bool):
    if isinstance(property_val, str):
        if property_val.lower() in ("1", "true", "t", "yes", "y", "on"):
            property_val = True
        elif property_val.lower() in ("0", "false", "f", "no", "n", "off"):
            property_val = False
        else:
            raise ValueError(
                "Invalid string value for bool type: %s" % property_val)
    else:
        property_val = bool(property_val)
elif isinstance(orig_val, int):
    property_val = int(property_val)
elif isinstance(orig_val, str):
    property_val = str(property_val)
else:
    raise TypeError("Unsupported property type: %s" % type(orig_val))
self._config[property_name] = property_val
self._save_to_file()

# Invoke set-callback.
if property_name in self._set_callbacks:
    self._set_callbacks[property_name](self._config)
