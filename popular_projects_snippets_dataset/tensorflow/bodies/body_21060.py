# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Test case for https://github.com/tensorflow/tensorflow/issues/12224
# where close() inside the with should have a better error message.
with self.assertRaisesRegex(RuntimeError, 'Session is already closed'):
    with monitored_session.MonitoredSession() as session:
        session.close()
