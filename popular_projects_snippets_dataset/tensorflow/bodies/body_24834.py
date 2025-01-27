# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
self.assertEqual("a", debug_graphs.get_node_name("a:0"))
self.assertEqual(0, debug_graphs.get_output_slot("a:0"))

self.assertEqual("_b", debug_graphs.get_node_name("_b:1"))
self.assertEqual(1, debug_graphs.get_output_slot("_b:1"))
