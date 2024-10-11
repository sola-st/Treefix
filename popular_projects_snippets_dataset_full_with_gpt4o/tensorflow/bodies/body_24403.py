# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
u_name, _, _, dump = self._session_run_for_graph_structure_lookup()

# Test num_devices().
self.assertEqual(self._expected_num_devices, len(dump.devices()))

# Test node_device().
self.assertEqual(self._main_device, dump.node_device(u_name))

with self.assertRaisesRegexp(ValueError,
                             "does not exist in partition graphs"):
    dump.node_device(u_name + "foo")

# Test node_exists().
self.assertTrue(dump.node_exists(u_name))
self.assertTrue(dump.node_exists(u_name + "/read"))
self.assertFalse(dump.node_exists(u_name + "/read" + "/foo"))
