# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
u_name, v_name, w_name, dump = (
    self._session_run_for_graph_structure_lookup())

# Test querying the debug watch keys with node names.
self.assertEqual(["%s:0:DebugIdentity" % u_name],
                 dump.debug_watch_keys(u_name))
self.assertEqual(["%s:0:DebugIdentity" % v_name],
                 dump.debug_watch_keys(v_name))
self.assertEqual(["%s:0:DebugIdentity" % w_name],
                 dump.debug_watch_keys(w_name))
self.assertEqual([], dump.debug_watch_keys("foo"))

# Test querying debug datum instances from debug watch.
u_data = dump.watch_key_to_data(dump.debug_watch_keys(u_name)[0])
self.assertEqual(1, len(u_data))
self.assertEqual(u_name, u_data[0].node_name)
self.assertEqual(0, u_data[0].output_slot)
self.assertEqual("DebugIdentity", u_data[0].debug_op)
self.assertGreaterEqual(u_data[0].timestamp, 0)
self.assertEqual([], dump.watch_key_to_data("foo"))
