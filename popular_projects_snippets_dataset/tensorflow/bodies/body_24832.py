# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
node_name, slot = debug_graphs.parse_node_or_tensor_name(
    "namespace1/node_1")

self.assertEqual("namespace1/node_1", node_name)
self.assertIsNone(slot)
