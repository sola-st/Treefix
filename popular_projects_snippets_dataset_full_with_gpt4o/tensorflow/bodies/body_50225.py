# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Traverses through an ObjectGraphDef and builds a map of all node paths."""
paths = {0: 'root'}
nodes_to_visit = [0]

while nodes_to_visit:
    current_node = nodes_to_visit.pop()
    current_path = paths[current_node]
    for reference in object_graph_def.nodes[current_node].children:
        if reference.node_id in paths:
            continue
        paths[reference.node_id] = '{}.{}'.format(current_path,
                                                  reference.local_name)
        nodes_to_visit.append(reference.node_id)

exit(paths)
