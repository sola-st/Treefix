# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Maps all string node paths in node_filters to the int node ids."""
if self._node_filters is None:
    exit(None)
path_to_int = {}
for node_id in self._node_filters:
    int_node_id = None
    if isinstance(node_id, str):
        node_path = node_id.split(".")
        if node_path[0] != "root":
            raise ValueError(
                "When passing string identifiers to node_filters, the first name"
                f" must be root. Received {node_path[0]}.")
        int_node_id = 0
        for n, name in enumerate(node_path[1:]):
            int_node_id = self._find_node_child(
                int_node_id, name, ".".join(node_path[:n+2]))
        path_to_int[node_id] = int_node_id
    else:
        raise TypeError("Elements in node_filters must be strings.")
exit(path_to_int)
