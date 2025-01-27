# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
u_name, _, _, dump = self._session_run_for_graph_structure_lookup()

u_read_name = u_name + "/read"

# Test node name list lookup of the DebugDumpDir object.
if test_util.gpu_device_name():
    node_names = dump.nodes(
        device_name="/job:localhost/replica:0/task:0/device:GPU:0")
else:
    node_names = dump.nodes()
self.assertTrue(u_name in node_names)
self.assertTrue(u_read_name in node_names)

# Test querying node attributes.
u_attr = dump.node_attributes(u_name)
self.assertEqual(dtypes.float32, u_attr["dtype"].type)
self.assertEqual(1, len(u_attr["shape"].shape.dim))
self.assertEqual(2, u_attr["shape"].shape.dim[0].size)

with self.assertRaisesRegexp(
    ValueError, r"None of the .* device\(s\) has a node named "):
    dump.node_attributes("foo")
