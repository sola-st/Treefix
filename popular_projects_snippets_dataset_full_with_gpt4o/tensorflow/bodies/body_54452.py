# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
graph = ops.Graph()
node = ops._NodeDef("b", "a_b")
weight_params = ops.get_stats_for_node_def(graph, node, "weight_params")
self.assertEqual(None, weight_params.value)
