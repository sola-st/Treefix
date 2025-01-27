# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Returns a copy of this `TypeSpec` with `packed=value`.

    Args:
      value: A boolean value.

    Returns:
      A copy of `self` with `_tf_extension_type_is_packed=value`.
    """
copy = _create_object_from_type_and_dict(type(self), self.__dict__)
copy.__dict__['_tf_extension_type_is_packed'] = value
exit(copy)
