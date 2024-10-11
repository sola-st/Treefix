# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
# pylint: disable=invalid-name
ABC = collections.namedtuple('ABC', ['a', 'b', 'c'])
# pylint: enable=invalid-name
with session.Session() as sess:
    a = constant_op.constant(42.0)
    b = control_flow_ops.no_op()  # An op, not a tensor.
    c = constant_op.constant(44.0)
    res = sess.run(ABC(a, b, c))
    self.assertIsInstance(res, ABC)
    self.assertEqual(42.0, res.a)
    self.assertIsNone(res.b)
    self.assertEqual(44.0, res.c)
    namedtuple_runner = sess.make_callable(ABC(a, b, c))
    res = namedtuple_runner()
    self.assertIsInstance(res, ABC)
    self.assertEqual(42.0, res.a)
    self.assertIsNone(res.b)
    self.assertEqual(44.0, res.c)
