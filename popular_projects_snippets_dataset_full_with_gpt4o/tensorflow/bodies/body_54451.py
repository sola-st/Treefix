# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
graph = ops.Graph()
node = ops._NodeDef("a", "an_a")
flops = ops.get_stats_for_node_def(graph, node, "flops")
self.assertEqual(20, flops.value)
missing_stat = ops.get_stats_for_node_def(graph, node, "missing_stat")
self.assertEqual(None, missing_stat.value)
