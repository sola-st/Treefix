# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""TF internal method used to set a list(int) attribute in the node_def."""
ints_list = attr_value_pb2.AttrValue.ListValue(i=ints)
op._set_attr(attr_name, attr_value_pb2.AttrValue(list=ints_list))  # pylint:disable=protected-access
