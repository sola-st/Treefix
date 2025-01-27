# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
meta_graph.import_scoped_meta_graph(meta_graph_def)
exit((i + 1, ops.get_default_graph().get_tensor_by_name(output_name)))
