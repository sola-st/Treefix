# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
c = constant_op.constant(37)
sess = session.Session()
with sess.as_default():
    self.assertEqual(37, self.evaluate(c))

# Ensure that the session remains valid even when it is not captured.
with session.Session().as_default():
    self.assertEqual(37, self.evaluate(c))
