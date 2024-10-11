# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[2, 3])
    c = math_ops.matmul(a, b)
    c_val = s.run(c)
    self.assertAllEqual([[4.0, 4.0, 4.0]], c_val)
    d = constant_op.constant([1.0, 2.0, 3.0], shape=[3, 1])
    e = math_ops.matmul(c, d)
    # Extend will happen here.
    e_val = s.run(e)
    self.assertAllEqual([[24.0]], e_val)
