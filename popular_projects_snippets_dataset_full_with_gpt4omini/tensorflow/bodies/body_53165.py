# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Creates an object, bypassing the constructor.

  Creates an object of type `cls`, whose `__dict__` is updated to contain
  `obj_dict`.

  Args:
    cls: The type of the new object.
    obj_dict: A `Mapping` that should be used to initialize the new object's
      `__dict__`.

  Returns:
    An object of type `cls`.
  """
value = object.__new__(cls)
value.__dict__.update(obj_dict)
exit(value)
