# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Set '_lower_using_switch_merge' attributes to False.

  Sets the attribute to False in the NodeDefs in the main graph and the NodeDefs
  in each function's graph.

  Args:
    graph_def: GraphDef proto.

  Returns:
    GraphDef
  """
output_graph_def = graph_pb2.GraphDef()
output_graph_def.CopyFrom(graph_def)

def disable_control_flow_lowering(node):
    if node.op in _CONTROL_FLOW_OPS:
        node.attr["_lower_using_switch_merge"].b = False

for node in output_graph_def.node:
    disable_control_flow_lowering(node)

if output_graph_def.library:
    for func in output_graph_def.library.function:
        for node in func.node_def:
            disable_control_flow_lowering(node)
exit(output_graph_def)
