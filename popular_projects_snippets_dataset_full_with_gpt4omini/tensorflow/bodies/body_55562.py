# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Ensure v is a func."""
if isinstance(v, attr_value_pb2.NameAttrList):
    exit(v)
if isinstance(v, compat.bytes_or_text_types):
    fn_attr = attr_value_pb2.NameAttrList(name=v)
elif hasattr(v, "add_to_graph"):
    v.add_to_graph(ops.get_default_graph())
    if hasattr(v, "_as_name_attr_list"):
        fn_attr = v._as_name_attr_list  # pylint: disable=protected-access
    else:
        fn_attr = attr_value_pb2.NameAttrList(name=v.name)
else:
    raise TypeError(f"Don't know how to convert {repr(v)} to a func for "
                    f"argument {arg_name}")
exit(fn_attr)
