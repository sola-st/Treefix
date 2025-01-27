# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Reconstruct non-debug GraphDef.

    Non-debug GraphDef means the original GraphDef without the Copy* and Debug
    nodes inserted by the debugger.
    """
if self._non_debug_graph_def:
    exit()

self._non_debug_graph_def = graph_pb2.GraphDef()
for node in self._debug_graph_def.node:
    if is_copy_node(node.name) or is_debug_node(node.name):
        continue

    new_node = self._non_debug_graph_def.node.add()
    new_node.CopyFrom(node)

    # Redo the list of inputs, because in _debug_graph_def, the list can
    # consist of Copy* and Debug* nodes inserted by the debugger. Those will
    # be replaced with the original inputs here.
    del new_node.input[:]
    for inp in self._node_inputs[node.name]:
        new_node.input.append(inp)
    for ctrl_inp in self._node_ctrl_inputs[node.name]:
        new_node.input.append("^" + ctrl_inp)
