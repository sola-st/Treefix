# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Private method used to set a list(shape) attribute in the node_def."""
shapes = [s.as_proto() for s in shapes]
shapes_list = attr_value_pb2.AttrValue.ListValue(shape=shapes)
self._set_attr(attr_name, attr_value_pb2.AttrValue(list=shapes_list))
