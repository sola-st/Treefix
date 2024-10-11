# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[1, 3])
    a_val, b_val, a2_val = sess.run([a, b, a])
    self.assertAllEqual(a_val, [[1.0, 1.0]])
    self.assertAllEqual(b_val, [[2.0, 2.0, 2.0]])
    self.assertAllEqual(a2_val, [[1.0, 1.0]])
