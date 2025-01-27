# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Extracts `output_structure`. For use in _apply_op_helper."""
for arg in op_def.output_arg:
    if arg.number_attr:
        n = _AttrValue(attr_protos, arg.number_attr, op_type_name).i
        output_structure.append(n)
    elif arg.type_attr:
        t = _AttrValue(attr_protos, arg.type_attr, op_type_name)
        output_structure.append(None)
    elif arg.type_list_attr:
        t = _AttrValue(attr_protos, arg.type_list_attr, op_type_name)
        output_structure.append(len(t.list.type))
    else:
        output_structure.append(None)
