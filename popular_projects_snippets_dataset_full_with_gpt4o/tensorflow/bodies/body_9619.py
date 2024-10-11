# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    res = sess.run(a.name)
    self.assertEqual(42.0, res)
    res = sess.run(a.op)  # An op, not a tensor.
    self.assertIsNone(res)
