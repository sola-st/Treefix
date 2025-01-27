# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
sess = session.Session()
with self.assertRaisesRegex(RuntimeError, 'not re-entrant'):
    with sess:
        with sess:
            pass
