# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Replace functions calls and shared names in `node_def`."""
if node_def.op in functions:
    node_def.op = functions[node_def.op].name
for _, attr_value in node_def.attr.items():
    if attr_value.WhichOneof("value") == "func":
        attr_value.func.name = functions[attr_value.func.name].name
    elif attr_value.WhichOneof("value") == "list":
        for fn in attr_value.list.func:
            fn.name = functions[fn.name].name

  # Fix old table creation bug.
if node_def.op == "HashTableV2":
    if ("use_node_name_sharing" not in node_def.attr or
        not node_def.attr["use_node_name_sharing"].b):
        node_def.attr["use_node_name_sharing"].b = True
        # We are turning on node mame sharing, so have to make sure we don't
        # accidentally share a table resource.
        shared_name_suffix += "_{}".format(ops.uid())

  # TODO(b/124205571): Avoid accidental sharing and destruction of restored
  # resources. For now uniquify "shared_name" when loading functions to avoid
  # sharing.
  # TODO: Add regression test for b/150826922.
op_def = op_def_registry.get(node_def.op)
if op_def:
    attr = next((a for a in op_def.attr if a.name == "shared_name"), None)
    if attr:
        shared_name = None
        if "shared_name" in node_def.attr and node_def.attr["shared_name"].s:
            shared_name = node_def.attr["shared_name"].s
        elif attr.default_value.s:
            shared_name = compat.as_bytes(attr.default_value.s)
        if not shared_name:
            shared_name = compat.as_bytes(node_def.name)

        node_def.attr["shared_name"].s = (
            shared_name + compat.as_bytes(shared_name_suffix))
