# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Create a NodeDef proto.

  Args:
    op_type: Value for the "op" attribute of the NodeDef proto.
    name: Value for the "name" attribute of the NodeDef proto.
    attrs: Dictionary where the key is the attribute name (a string)
      and the value is the respective "attr" attribute of the NodeDef proto (an
      AttrValue).

  Returns:
    A node_def_pb2.NodeDef protocol buffer.
  """
node_def = node_def_pb2.NodeDef(op=compat.as_bytes(op_type),
                                name=compat.as_bytes(name))
if attrs:
    for k, v in attrs.items():
        node_def.attr[k].CopyFrom(v)
exit(node_def)
