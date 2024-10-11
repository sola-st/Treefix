# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Check if an object is of the expected type.

  Args:
    obj: The object being checked.
    expected_types: (`type` or an iterable of `type`s) The expected `type`(s)
      of obj.

  Raises:
      TypeError: If obj is not an instance of expected_type.
  """
if not isinstance(obj, expected_types):
    raise TypeError("Expected type %s; got type %s" %
                    (expected_types, type(obj)))
