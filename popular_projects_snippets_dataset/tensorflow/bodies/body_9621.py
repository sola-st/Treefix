# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    b = control_flow_ops.no_op()  # An op, not a tensor.
    c = constant_op.constant(44.0)
    res = sess.run((a, b, c, a.name))
    self.assertIsInstance(res, tuple)
    self.assertEqual((42.0, None, 44.0, 42.0), res)
    tuple_runner = sess.make_callable((a, b, c, a.name))
    res = tuple_runner()
    self.assertIsInstance(res, tuple)
    self.assertEqual((42.0, None, 44.0, 42.0), res)
