# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
invalid_debug_node_name_1 = "__dbg_node1_0_DebugIdentity"

with self.assertRaisesRegex(ValueError,
                            "Invalid tensor name in debug node name"):
    debug_graphs.parse_debug_node_name(invalid_debug_node_name_1)
