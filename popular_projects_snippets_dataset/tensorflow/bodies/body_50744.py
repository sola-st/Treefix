# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Adds edges from objects to other objects and functions."""
for node_id, object_proto in self._iter_all_nodes():
    self._add_object_graph_edges(object_proto, node_id)

# If root object isn't loaded, then create edges from the root for
# checkpoint compatibility.
if self._filtered_nodes is not None and 0 not in self._filtered_nodes:
    root = self.get(0)
    for node_path in self._node_filters:
        loaded_node = self._nodes[self._node_path_to_id[node_path]]
        path = node_path.split(".")
        current_node = root
        for name in path[1:-1]:
            if not hasattr(current_node, name):
                setattr(current_node, name, self._recreate_base_user_object()[0])
            current_node = getattr(current_node, name)
        if not hasattr(current_node, path[-1]):
            setattr(current_node, path[-1], loaded_node)
