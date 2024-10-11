# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
# Reinitialize the global state to ensure that the expected warnings will
# be emitted.
session.InteractiveSession._active_session_count = 0  # pylint: disable=protected-access

sess = session.InteractiveSession()
sess.run(constant_op.constant(4.0))  # Run so that the session is "opened".
sess.close()
# Opening and closing interactive sessions serially should not warn.
with warnings.catch_warnings(record=True) as w:
    sess = session.InteractiveSession()
    sess.close()
self.assertEqual(0, len(w))

with warnings.catch_warnings(record=True) as w:
    sess = session.InteractiveSession()
self.assertEqual(0, len(w))
with warnings.catch_warnings(record=True) as w:
    sess2 = session.InteractiveSession()
self.assertEqual(1, len(w))
self.assertIn('An interactive session is already active. This can cause '
              'out-of-memory errors in some cases. You must explicitly '
              'call `InteractiveSession.close()` to release resources '
              'held by the other session(s).', str(w[0].message))
sess2.close()
sess.close()
