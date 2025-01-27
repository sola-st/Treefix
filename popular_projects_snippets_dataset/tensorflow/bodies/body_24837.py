# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
self.assertTrue(
    debug_graphs.is_debug_node("__dbg_ns1/ns2/node3:0_0_DebugIdentity"))

self.assertFalse(
    debug_graphs.is_debug_node("dbg_ns1/ns2/node3:0_0_DebugIdentity"))
self.assertFalse(
    debug_graphs.is_debug_node("_dbg_ns1/ns2/node3:0_0_DebugIdentity"))
self.assertFalse(
    debug_graphs.is_debug_node("_dbgns1/ns2/node3:0_0_DebugIdentity"))
self.assertFalse(debug_graphs.is_debug_node("__copy_ns1/ns2/node3_0"))
