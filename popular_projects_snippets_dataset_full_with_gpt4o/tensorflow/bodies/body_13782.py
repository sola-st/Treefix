# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Initializes the AppendDocstring object.

    Args:
      additional_note: Python string added as additional docstring to public
        version of function.
      kwargs_dict: Python string/string dictionary representing specific kwargs
        expanded from the **kwargs input.

    Raises:
      ValueError: if kwargs_dict.key contains whitespace.
      ValueError: if kwargs_dict.value contains newlines.
    """
self._additional_note = additional_note
if kwargs_dict:
    bullets = []
    for key in sorted(kwargs_dict.keys()):
        value = kwargs_dict[key]
        if any(x.isspace() for x in key):
            raise ValueError("Parameter name \"%s\" contains whitespace." % key)
        value = value.lstrip()
        if "\n" in value:
            raise ValueError(
                "Parameter description for \"%s\" contains newlines." % key)
        bullets.append("*  `%s`: %s" % (key, value))
    self._additional_note += ("\n\n##### `kwargs`:\n\n" + "\n".join(bullets))
