# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
for node_def in graph_def.node:
    if (debug_graphs.is_debug_node(node_def.name) and
        node_def.attr["gated_grpc"].b):
        node_name, output_slot, _, debug_op = (
            debug_graphs.parse_debug_node_name(node_def.name))
        self._gated_grpc_debug_watches.add(
            DebugWatch(node_name, output_slot, debug_op))
