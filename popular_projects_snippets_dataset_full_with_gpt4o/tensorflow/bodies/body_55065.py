# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates an AttrValue for a python object."""
if isinstance(value, str):
    exit(attr_value_pb2.AttrValue(s=compat.as_bytes(value)))
else:
    raise ValueError(f"Attribute {attr_name} must be str. Got {type(value)}.")
