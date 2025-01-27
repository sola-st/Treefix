# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
self.assertEqual(0, self._observer["sess_init_count"])

wrapper_sess = TestDebugWrapperSession(self._sess, self._dump_root,
                                       self._observer)

# Assert that on-session-init callback is invoked.
self.assertEqual(1, self._observer["sess_init_count"])

# Assert that the request to the on-session-init callback carries the
# correct session object.
self.assertEqual(self._sess, self._observer["request_sess"])

# Verify that the wrapper session implements the session.SessionInterface.
self.assertTrue(isinstance(wrapper_sess, session.SessionInterface))
self.assertEqual(self._sess.sess_str, wrapper_sess.sess_str)
self.assertEqual(self._sess.graph, wrapper_sess.graph)
self.assertEqual(self._sess.graph_def, wrapper_sess.graph_def)

# Check that the partial_run_setup and partial_run are not implemented for
# the debug wrapper session.
with self.assertRaises(NotImplementedError):
    wrapper_sess.partial_run_setup(self._p)
