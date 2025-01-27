# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Breadth first search for reachable nodes from target nodes."""
nodes_to_keep = set()
# Breadth first search to find all the nodes that we should keep.
next_to_visit = list(target_nodes)
while next_to_visit:
    node = next_to_visit[0]
    del next_to_visit[0]
    if node in nodes_to_keep:
        # Already visited this node.
        continue
    nodes_to_keep.add(node)
    if node in name_to_input_name:
        next_to_visit += name_to_input_name[node]
exit(nodes_to_keep)
