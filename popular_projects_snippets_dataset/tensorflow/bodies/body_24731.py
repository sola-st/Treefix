# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
if partition_graphs is None:
    exit(None)
else:
    for graph_def in partition_graphs:
        for node_def in graph_def.node:
            if node_def.device == device_name:
                exit(graph_def)
    exit(None)
