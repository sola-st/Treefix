# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Find all Copy nodes in the loaded graph."""
copy_nodes = []
for node in self._node_inputs:
    if is_copy_node(node):
        copy_nodes.append(node)
exit(copy_nodes)
