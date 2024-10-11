# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
assertion = control_flow_ops.Assert(False, ['This should fail.'])
with self.cached_session() as sess:
    coord = coordinator.Coordinator(clean_stop_exception_types=())
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    try:
        coord_sess.run([assertion])
        self.fail('No exception was raised by assertion.')
    except errors_impl.InvalidArgumentError:
        # Extract the name of the file where the exception was first raised.
        _, _, exc_traceback = sys.exc_info()
        tb = traceback.extract_tb(exc_traceback)
        exc_source_file = tb[-1][0]
        exc_source_basename = os.path.basename(exc_source_file)
        # If it's monitored_session.py then the original stack trace was not
        # correctly propagated.
        self.assertIn(
            exc_source_basename, ['session.py', 'monitored_session.py'],
            'The exception was raised from an unrecognized file. This unit '
            'test probably needs to be updated. Traceback:\n%s\n' % tb)
        self.assertEqual(
            exc_source_basename, 'session.py',
            'Original stack trace was not propagated by MonitoredSession. '
            'Traceback:\n%s' % tb)
