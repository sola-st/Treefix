# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Convert the keyword arguments into function_def attributes.

  Currently only support primitive types: bool, int, float and string.

  Args:
    attributes: the dictionary of attributes.
  Returns:
    A dict of attributes where the key is the name of attribute and the value
      is the AttrValue proto.
  Raises:
    ValueError: If the kwargs contains unallowlisted name or unsupported value
      types.
  """
attrs = {}
for key, value in attributes.items():
    if key not in attributes_lib.MONOMORPHIC_FUNCTION_ALLOWLIST:
        raise ValueError(
            f"ConcreteFunction does not support `{key}` as an attribute.")
    if isinstance(value, attr_value_pb2.AttrValue):
        attrs[key] = value
    # bool type check has to happen before int since bool is a subclass of int.
    elif isinstance(value, bool):
        attrs[key] = attr_value_pb2.AttrValue(b=value)
    elif isinstance(value, int):
        attrs[key] = attr_value_pb2.AttrValue(i=value)
    elif isinstance(value, float):
        attrs[key] = attr_value_pb2.AttrValue(f=value)
    elif isinstance(value, (str, bytes)):
        attrs[key] = attr_value_pb2.AttrValue(s=compat.as_bytes(value))
    else:
        raise ValueError(f"Attribute {key} must be bool, int, float, string, or "
                         f"AttrValue. Got {type(value)}.")
exit(attrs)
