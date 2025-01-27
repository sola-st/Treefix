# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
sess1 = session.Session()
sess1_controller = sess1.as_default()
sess1_controller.__enter__()

sess2 = session.Session()
sess2_controller = sess2.as_default()
sess2_controller.__enter__()

with self.assertRaisesRegex(AssertionError, 'Nesting violated'):
    sess1_controller.__exit__(None, None, None)

ops._default_session_stack.reset()
