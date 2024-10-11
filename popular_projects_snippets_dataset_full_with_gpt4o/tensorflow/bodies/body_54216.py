# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Create a `NodeDef` proto with export_scope stripped.

  Args:
    from_node_def: A `node_def_pb2.NodeDef` protocol buffer.
    export_scope: A `string` representing the name scope to remove.
    unbound_inputs: An array of unbound input names if they exist.
    clear_devices: Boolean which controls whether to clear device information
      from node_def. Default false.

  Returns:
    A `node_def_pb2.NodeDef` protocol buffer.
  """
node_def = copy.deepcopy(from_node_def)
for i, v in enumerate(node_def.input):
    if (export_scope and
        not node_def.input[i].lstrip("^").startswith(export_scope)):
        # Adds "$unbound_inputs_" prefix to the unbound name so they are easily
        # identifiable.
        node_def.input[i] = re.sub(r"([\^]|^)(.*)",
                                   r"\1" + _UNBOUND_INPUT_PREFIX + r"\2",
                                   compat.as_str(v))
        unbound_inputs.append(node_def.input[i])
    else:
        node_def.input[i] = ops.strip_name_scope(v, export_scope)
node_def.name = compat.as_bytes(
    ops.strip_name_scope(from_node_def.name, export_scope))
for k, v in from_node_def.attr.items():
    if k == "_class":
        new_s = [compat.as_bytes(
            ops.strip_name_scope(s, export_scope)) for s in v.list.s
                 if not export_scope or
                 compat.as_str(s).split("@")[1].startswith(export_scope)]
        node_def.attr[k].CopyFrom(attr_value_pb2.AttrValue(
            list=attr_value_pb2.AttrValue.ListValue(s=new_s)))
    elif node_def.op in ("Enter", "RefEnter") and k == "frame_name":
        if not export_scope or compat.as_str(v.s).startswith(export_scope):
            new_s = compat.as_bytes(ops.strip_name_scope(v.s, export_scope))
        node_def.attr[k].CopyFrom(attr_value_pb2.AttrValue(s=new_s))
    else:
        node_def.attr[k].CopyFrom(v)

if clear_devices:
    node_def.device = ""

exit(node_def)
