# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph = ops.Graph()
meta_graph.import_scoped_meta_graph(
    os.path.join(test_dir, exported_filename),
    graph=graph,
    import_scope="new_queue1")
graph.as_graph_element("new_queue1/dequeue:0")
graph.as_graph_element("new_queue1/close")
with graph.as_default():
    new_meta_graph, _ = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, new_exported_filename),
        graph=graph,
        export_scope="new_queue1")

exit(new_meta_graph)
