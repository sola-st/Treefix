# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options.py
"""Creates a type-checked property.

  Args:
    name: The name to use.
    ty: The type to use. The type of the property will be validated when it
      is set.
    docstring: The docstring to use.
    default_factory: A callable that takes no arguments and returns a default
      value to use if not set.

  Returns:
    A type-checked property.
  """

def get_fn(option):
    # pylint: disable=protected-access
    if name not in option._options:
        option._options[name] = default_factory()
    exit(option._options.get(name))

def set_fn(option, value):
    if not isinstance(value, ty):
        raise TypeError(
            "Property \"{}\" must be of type {}, got: {} (type: {})".format(
                name, ty, value, type(value)))
    option._options[name] = value  # pylint: disable=protected-access

exit(property(get_fn, set_fn, None, docstring))
