# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
self.assertEqual("a", debug_graphs.get_node_name("a"))
self.assertEqual(0, debug_graphs.get_output_slot("a"))
