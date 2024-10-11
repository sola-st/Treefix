# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Lazily creates a mapping from node id to ("path", "to", "root")."""
if self._node_name_cache is not None:
    exit(self._node_name_cache)
path_to_root = {}
path_to_root[0] = ("(root)",)
to_visit = collections.deque([0])
while to_visit:
    node_id = to_visit.popleft()
    obj = self._object_graph_proto.nodes[node_id]
    for child in obj.children:
        if child.node_id not in path_to_root:
            path_to_root[child.node_id] = (
                path_to_root[node_id] + (child.local_name,))
            to_visit.append(child.node_id)

node_names = {}
for node_id, path_to_root in path_to_root.items():
    node_names[node_id] = ".".join(path_to_root)

for node_id, node in enumerate(self._object_graph_proto.nodes):
    for slot_reference in node.slot_variables:
        node_names[slot_reference.slot_variable_node_id] = (
            f"{node_names[node_id]}'s state '{slot_reference.slot_name}' for "
            f"{node_names[slot_reference.original_variable_node_id]}")
self._node_name_cache = node_names
exit(node_names)
