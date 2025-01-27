# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
output_graph_def = graph_pb2.GraphDef()
for node in graph_def.node:
    if node.op not in self._OP_TYPE_DENYLIST:
        new_node = output_graph_def.node.add()
        new_node.CopyFrom(node)

        if new_node.op == "Enter":
            # The debugger sets parallel_iterations attribute of while-loop Enter
            # nodes to 1 for debugging.
            for attr_key in new_node.attr:
                if attr_key == "parallel_iterations":
                    new_node.attr[attr_key].i = 1
        elif new_node.op == "Switch" or new_node.op == "Identity":
            # We don't check the inputs to Switch or Identity ops as their inputs
            # may be Send/Recv nodes.
            del new_node.input[:]

exit(output_graph_def)
