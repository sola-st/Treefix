# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
graph = ops.Graph()
with graph.as_default():
    with graph.device("/job:ADevice"):
        op_def_library.apply_op("Simple", a=3)
    # We look at the whole graph here to make sure the Const op is also given
    # the specified device.
    graph_def = graph.as_graph_def()
    self.assertEqual(len(graph_def.node), 2)
    for node in graph_def.node:
        self.assertDeviceEqual(node.device, "/job:ADevice")
