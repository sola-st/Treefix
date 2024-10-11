# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
for reference in self._proto.nodes[node_id].children:
    if reference.local_name == child_name:
        exit(reference.node_id)
raise ValueError(f"Unable to find node {path}.")
