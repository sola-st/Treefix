# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    res = sess.run(a)
    self.assertEqual(42.0, res)
    res = sess.run(a.op)  # An op, not a tensor.
    self.assertIsNone(res)
    tensor_runner = sess.make_callable(a)
    res = tensor_runner()
    self.assertEqual(42.0, res)
    op_runner = sess.make_callable(a.op)
    res = op_runner()
    self.assertIsNone(res)
