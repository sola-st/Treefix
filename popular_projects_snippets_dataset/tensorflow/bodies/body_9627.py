# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a_val = 11.0
    a = constant_op.constant(a_val)

    res = sess.run([[], tuple(), {}])
    self.assertIsInstance(res, list)
    self.assertEqual(3, len(res))
    self.assertIsInstance(res[0], list)
    self.assertEqual(0, len(res[0]))
    self.assertIsInstance(res[1], tuple)
    self.assertEqual(0, len(res[1]))
    self.assertIsInstance(res[2], dict)
    self.assertEqual(0, len(res[2]))

    res = sess.run([[], tuple(), {}, a])
    self.assertIsInstance(res, list)
    self.assertEqual(4, len(res))
    self.assertIsInstance(res[0], list)
    self.assertEqual(0, len(res[0]))
    self.assertIsInstance(res[1], tuple)
    self.assertEqual(0, len(res[1]))
    self.assertIsInstance(res[2], dict)
    self.assertEqual(0, len(res[2]))
    self.assertEqual(a_val, res[3])
