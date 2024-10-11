# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
u_name, v_name, w_name, dump = (
    self._session_run_for_graph_structure_lookup())

u_read_name = u_name + "/read"

# Test the inputs lookup of the DebugDumpDir object.
self.assertEqual([], dump.node_inputs(u_name))
self.assertEqual([u_name], dump.node_inputs(u_read_name))
self.assertEqual([u_read_name] * 2, dump.node_inputs(v_name))
self.assertEqual([v_name] * 2, dump.node_inputs(w_name))

self.assertEqual([], dump.node_inputs(u_name, is_control=True))
self.assertEqual([], dump.node_inputs(u_read_name, is_control=True))
self.assertEqual([], dump.node_inputs(v_name, is_control=True))
self.assertEqual([], dump.node_inputs(w_name, is_control=True))

# Test the outputs recipient lookup of the DebugDumpDir object.
self.assertTrue(u_read_name in dump.node_recipients(u_name))
self.assertEqual(2, dump.node_recipients(u_read_name).count(v_name))
self.assertEqual(2, dump.node_recipients(v_name).count(w_name))

self.assertEqual([], dump.node_recipients(u_name, is_control=True))
self.assertEqual([], dump.node_recipients(u_read_name, is_control=True))
self.assertEqual([], dump.node_recipients(v_name, is_control=True))
self.assertEqual([], dump.node_recipients(w_name, is_control=True))

# Test errors raised on invalid node names.
with self.assertRaisesRegexp(
    ValueError, r"None of the .* device\(s\) has a node named "):
    dump.node_inputs(u_name + "foo")
with self.assertRaisesRegexp(
    ValueError, r"None of the .* device\(s\) has a node named "):
    dump.node_recipients(u_name + "foo")

# Test transitive_inputs().
self.assertEqual([], dump.transitive_inputs(u_name))
self.assertEqual([u_name], dump.transitive_inputs(u_read_name))
self.assertEqual(
    set([u_name, u_read_name]), set(dump.transitive_inputs(v_name)))
self.assertEqual(
    set([u_name, u_read_name, v_name]), set(dump.transitive_inputs(w_name)))

with self.assertRaisesRegexp(
    ValueError, r"None of the .* device\(s\) has a node named "):
    dump.transitive_inputs(u_name + "foo")
