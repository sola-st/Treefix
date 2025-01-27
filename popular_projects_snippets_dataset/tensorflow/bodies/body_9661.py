# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    with self.assertRaisesRegex(RuntimeError, 'The Session graph is empty.'):
        sess.run([])
    with self.assertRaisesRegex(RuntimeError, 'The Session graph is empty.'):
        sess.run(())
    with self.assertRaisesRegex(RuntimeError, 'The Session graph is empty.'):
        sess.run({})
