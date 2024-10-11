# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Private method used to set a function attribute in the node_def."""
func = attr_value_pb2.NameAttrList(name=func_name)
self._set_attr(attr_name, attr_value_pb2.AttrValue(func=func))
