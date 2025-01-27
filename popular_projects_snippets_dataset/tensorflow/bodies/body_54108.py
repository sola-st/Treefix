# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_to_function_def.py
"""Converts an op to a function def node and add it to `func`."""
# Add an entry in func.node_def

# Note that extend() makes a copy in this case, see:
# https://developers.google.com/protocol-buffers/docs/reference/python-generated#repeated-message-fields
func.node_def.extend([_get_node_def(op)])
node_def = func.node_def[-1]
for i in range(len(node_def.input)):
    if not node_def.input[i].startswith("^"):
        assert node_def.input[i] in input_dict, ("%s missing from %s" %
                                                 (node_def.input[i],
                                                  input_dict.items()))
        node_def.input[i] = input_dict[node_def.input[i]]
  # The function is stateful if any of its operations are stateful.
  # NOTE(mrry): The "Const" node typically does not have an `OpDef` associated
  # with it, so we assume any nodes without an `OpDef` are stateless.
  # TODO(skyewm): Remove the `is not None` test after we transition to the C
  # API.
if op.op_def is not None and op.op_def.is_stateful:
    func.signature.is_stateful = True
