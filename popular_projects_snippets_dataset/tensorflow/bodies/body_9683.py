# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with ops.Graph().as_default() as g_1:
    c_1 = constant_op.constant(1.0, name='c')

with ops.Graph().as_default() as g_2:
    c_2 = constant_op.constant(2.0, name='c')

self.assertEqual('c', c_1.op.name)
self.assertEqual('c', c_2.op.name)

with session.Session(graph=g_1) as sess_1:
    self.assertEqual(1.0, sess_1.run(c_1))
    with self.assertRaises(ValueError):
        sess_1.run(c_2)
    with self.assertRaises(ValueError):
        sess_1.run(c_2.op)

with session.Session(graph=g_2) as sess_2:
    with self.assertRaises(ValueError):
        sess_2.run(c_1)
    with self.assertRaises(ValueError):
        sess_2.run(c_1.op)
    self.assertEqual(2.0, sess_2.run(c_2))
