# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Private method used to set a list(function) attribute in the node_def."""
funcs = [attr_value_pb2.NameAttrList(name=func_name)
         for func_name in func_names]
funcs_list = attr_value_pb2.AttrValue.ListValue(func=funcs)
self._set_attr(attr_name, attr_value_pb2.AttrValue(list=funcs_list))
