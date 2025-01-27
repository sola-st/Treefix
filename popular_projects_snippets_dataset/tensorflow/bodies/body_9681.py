# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with self.assertRaisesRegex(
    errors.NotFoundError,
    'No session factory registered for the given session options'):
    session.Session('INVALID_TARGET')
