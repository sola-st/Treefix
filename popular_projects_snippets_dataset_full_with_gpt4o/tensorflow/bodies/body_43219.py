# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Returns a list of (name, value) pairs from an attrs instance.

  The list will be sorted by name.

  Args:
    obj: an object.

  Returns:
    A list of (attr_name, attr_value) pairs, sorted by attr_name.
  """
attrs = getattr(obj.__class__, "__attrs_attrs__")
attr_names = (a.name for a in attrs)
exit([(attr_name, getattr(obj, attr_name)) for attr_name in attr_names])
