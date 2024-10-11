# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph1 = ops.Graph()
with graph1.as_default():
    with ops.device("/device:CPU:0"):
        a = variables.Variable(
            constant_op.constant(
                1.0, shape=[2, 2]), name="a")
    with ops.device("/job:ps/replica:0/task:0/device:GPU:0"):
        b = variables.Variable(
            constant_op.constant(
                2.0, shape=[2, 2]), name="b")
    with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
        math_ops.matmul(a, b, name="matmul")

self.assertEqual("/device:CPU:0", str(graph1.as_graph_element("a").device))
self.assertEqual("/job:ps/replica:0/task:0/device:GPU:0",
                 str(graph1.as_graph_element("b").device))
self.assertEqual("/job:localhost/replica:0/task:0/device:CPU:0",
                 str(graph1.as_graph_element("matmul").device))

# Verifies that devices are cleared on export.
orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(
    graph=graph1, clear_devices=True)

graph2 = ops.Graph()
with graph2.as_default():
    meta_graph.import_scoped_meta_graph(orig_meta_graph, clear_devices=False)

self.assertEqual("", str(graph2.as_graph_element("a").device))
self.assertEqual("", str(graph2.as_graph_element("b").device))
self.assertEqual("", str(graph2.as_graph_element("matmul").device))

# Verifies that devices are cleared on export when passing in graph_def.
orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(
    graph_def=graph1.as_graph_def(), clear_devices=True)

graph2 = ops.Graph()
with graph2.as_default():
    meta_graph.import_scoped_meta_graph(orig_meta_graph, clear_devices=False)

self.assertEqual("", str(graph2.as_graph_element("a").device))
self.assertEqual("", str(graph2.as_graph_element("b").device))
self.assertEqual("", str(graph2.as_graph_element("matmul").device))

# Verifies that devices are cleared on import.
orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(
    graph=graph1, clear_devices=False)

graph2 = ops.Graph()
with graph2.as_default():
    meta_graph.import_scoped_meta_graph(orig_meta_graph, clear_devices=True)

self.assertEqual("", str(graph2.as_graph_element("a").device))
self.assertEqual("", str(graph2.as_graph_element("b").device))
self.assertEqual("", str(graph2.as_graph_element("matmul").device))
