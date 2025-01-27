# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
node_name, slot = debug_graphs.parse_node_or_tensor_name(
    "namespace1/node_2:3")

self.assertEqual("namespace1/node_2", node_name)
self.assertEqual(3, slot)
