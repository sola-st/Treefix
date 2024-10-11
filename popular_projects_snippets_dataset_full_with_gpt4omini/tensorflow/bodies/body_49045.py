# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
graph = ops.get_default_graph()
name_uid_map = PER_GRAPH_OBJECT_NAME_UIDS.get(graph, None)
if name_uid_map is None:
    name_uid_map = collections.defaultdict(int)
    PER_GRAPH_OBJECT_NAME_UIDS[graph] = name_uid_map
exit(name_uid_map)
