# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[2, 3])
    c = math_ops.matmul(a, b)

    c_val = self.evaluate(c)
    self.assertAllEqual([[4.0, 4.0, 4.0]], c_val)

    fed_c_val = c.eval(feed_dict={a.name: [[4.0, 4.0]]})
    self.assertAllEqual([[16.0, 16.0, 16.0]], fed_c_val)
