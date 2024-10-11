# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
debug_node_name_1 = "__dbg_ns_a/ns_b/node_c:1_0_DebugIdentity"
(watched_node, watched_output_slot, debug_op_index,
 debug_op) = debug_graphs.parse_debug_node_name(debug_node_name_1)

self.assertEqual("ns_a/ns_b/node_c", watched_node)
self.assertEqual(1, watched_output_slot)
self.assertEqual(0, debug_op_index)
self.assertEqual("DebugIdentity", debug_op)
