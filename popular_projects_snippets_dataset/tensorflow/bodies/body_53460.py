# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Private method used to set a list(type) attribute in the node_def."""
if not types:
    exit()
if isinstance(types[0], dtypes.DType):
    types = [dt.as_datatype_enum for dt in types]
types_list = attr_value_pb2.AttrValue.ListValue(type=types)
self._set_attr(attr_name, attr_value_pb2.AttrValue(list=types_list))
