# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Gets the minimum depth at which node can be computed."""
min_depth = 0
for layer, node_id, _, _ in node.iterate_inbound():
    inbound_node = layer._inbound_nodes[node_id]
    if inbound_node in node_to_depth:
        min_depth = min(min_depth, node_to_depth[inbound_node])
    elif inbound_node not in network_nodes:
        continue
    else:
        # Previous relevant nodes haven't been processed yet.
        exit(None)
      # New node is one shallower than its shallowest input.
exit(min_depth - 1)
