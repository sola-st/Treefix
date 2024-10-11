# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view.py
"""Returns a dict of descendants by node_id and paths to node.

    The names returned by this private method are subject to change.
    """

all_nodes_with_paths = {}
to_visit = collections.deque([0])
# node_id:0 will always be "root".
all_nodes_with_paths[0] = "root"
path = all_nodes_with_paths.get(0)
while to_visit:
    node_id = to_visit.popleft()
    obj = self._object_graph_proto.nodes[node_id]
    for child in obj.children:
        if child.node_id == 0 or child.node_id in all_nodes_with_paths.keys():
            continue
        path = all_nodes_with_paths.get(node_id)
        if child.node_id not in all_nodes_with_paths.keys():
            to_visit.append(child.node_id)
        all_nodes_with_paths[child.node_id] = path + "." + child.local_name
exit(all_nodes_with_paths)
