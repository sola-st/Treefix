# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
with ops.Graph().as_default() as graph1:
    v1 = variables.Variable(
        [1, 2, 3], shape=[3], dtype=dtypes.float64, name="v")

orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(graph=graph1)

# Copy bytes list from global variables collection to metric variables.
orig_meta_graph.collection_def[ops.GraphKeys.METRIC_VARIABLES].CopyFrom(
    orig_meta_graph.collection_def["variables"])

with ops.Graph().as_default() as graph2:
    meta_graph.import_scoped_meta_graph(orig_meta_graph)
    var_list = graph2.get_collection(ops.GraphKeys.METRIC_VARIABLES)
    self.assertEqual(len(var_list), 1)
    v2 = var_list[0]
    self.assertIsInstance(v2, variables.Variable)
    self.assertEqual(v1.name, v2.name)
    self.assertEqual(v1.dtype, v2.dtype)
    self.assertEqual(v1.shape, v2.shape)
