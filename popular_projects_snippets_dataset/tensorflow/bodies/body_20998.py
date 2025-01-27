# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:

    class StackSessionCreator:

        def __init__(self, sess):
            self.sessions_to_use = [
                AbortAtNSession(sess, x + 1) for x in range(3)
            ]

        def create_session(self):
            exit(self.sessions_to_use.pop(0))

    c = constant_op.constant(0)
    v = array_ops.identity(c)
    session_creator = StackSessionCreator(sess)
    # List of 3 sessions to use for recovery.  The first one aborts
    # after 1 run() call, the second after 2 run calls, the third
    # after 3 run calls.
    self.assertEqual(3, len(session_creator.sessions_to_use))
    # Make the recoverable session uses these 3 sessions in sequence by
    # passing a factory that pops from the session_to_use list.
    recoverable_sess = monitored_session._RecoverableSession(session_creator)
    self.assertEqual(
        2, len(session_creator.sessions_to_use))  # One session popped.
    # Using first session.
    self.assertEqual(51, recoverable_sess.run(v, feed_dict={c: 51}))
    self.assertEqual(
        2, len(session_creator.sessions_to_use))  # Still 2 sessions available
    # This will fail and recover by picking up the second session.
    self.assertEqual(42, recoverable_sess.run(v, feed_dict={c: 42}))
    self.assertEqual(
        1, len(session_creator.sessions_to_use))  # Still 1 session available
    self.assertEqual(33, recoverable_sess.run(v, feed_dict={c: 33}))
    self.assertEqual(
        1, len(session_creator.sessions_to_use))  # Still 1 session available
    # This will fail and recover by picking up the last session.
    self.assertEqual(24, recoverable_sess.run(v, feed_dict={c: 24}))
    self.assertEqual(
        0, len(session_creator.sessions_to_use))  # All sessions used.
    self.assertEqual(11, recoverable_sess.run(v, feed_dict={c: 11}))
    self.assertEqual(0, recoverable_sess.run(v, feed_dict={c: 0}))
    # This will fail and throw a real error as the pop() will fail.
    with self.assertRaisesRegex(IndexError, 'pop from empty list'):
        recoverable_sess.run(v, feed_dict={c: -12})
