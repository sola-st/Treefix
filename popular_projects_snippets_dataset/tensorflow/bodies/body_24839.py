# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
invalid_debug_node_name_1 = "__copy_ns_a/ns_b/node_c:1_0_DebugIdentity"

with self.assertRaisesRegex(ValueError, "Invalid prefix"):
    debug_graphs.parse_debug_node_name(invalid_debug_node_name_1)
