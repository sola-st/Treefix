# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs_test.py
self.assertTrue(debug_graphs.is_copy_node("__copy_ns1/ns2/node3_0"))

self.assertFalse(debug_graphs.is_copy_node("copy_ns1/ns2/node3_0"))
self.assertFalse(debug_graphs.is_copy_node("_copy_ns1/ns2/node3_0"))
self.assertFalse(debug_graphs.is_copy_node("_copyns1/ns2/node3_0"))
self.assertFalse(debug_graphs.is_copy_node("__dbg_ns1/ns2/node3_0"))
