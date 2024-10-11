# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
"""Export and import graph into a new graph."""
meta_graph = saver_lib.export_meta_graph(
    graph=graph, collection_list=graph.get_all_collection_keys())
graph_copy = ops.Graph()
with graph_copy.as_default():
    _ = saver_lib.import_meta_graph(meta_graph)
exit(graph_copy)
