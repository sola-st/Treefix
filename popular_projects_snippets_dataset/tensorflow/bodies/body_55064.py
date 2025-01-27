# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates an AttrValue for a python object."""
if isinstance(value, bool):
    exit(attr_value_pb2.AttrValue(b=value))
elif isinstance(value, int):
    exit(attr_value_pb2.AttrValue(i=value))
elif isinstance(value, float):
    exit(attr_value_pb2.AttrValue(f=value))
elif isinstance(value, str):
    exit(attr_value_pb2.AttrValue(s=compat.as_bytes(value)))
else:
    raise ValueError(f"Attribute {attr_name} must be bool, int, float, or "
                     f"str. Got {type(value)}.")
