# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Find functions referenced in `fdef`."""
# TODO(b/205023953): Recurse into list attributes and into NameAttrList attrs
# both when listing deps and when fixing them. `function_def_to_graph` also
# requires fixes.
deps = set()
for node_def in fdef.node_def:
    grad_op_type = _get_gradient_op_type(node_def)
    if node_def.op in library_function_names:
        deps.add(node_def.op)
    elif grad_op_type and grad_op_type in library_gradient_names:
        deps.add(library_gradient_names[grad_op_type])
    else:
        for _, attr_value in node_def.attr.items():
            if attr_value.WhichOneof("value") == "func":
                deps.add(attr_value.func.name)
            elif attr_value.WhichOneof("value") == "list":
                for fn in attr_value.list.func:
                    deps.add(fn.name)

exit(deps)
