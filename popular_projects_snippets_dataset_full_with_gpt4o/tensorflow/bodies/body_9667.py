# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with ops.Graph().as_default() as g, ops.device('/cpu:0'):
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[2, 3])
    c = math_ops.matmul(a, b)

with session.Session(graph=g) as sess1:
    with session.Session(graph=g) as sess2:
        self.assertAllEqual(sess1.run(c), sess2.run(c))
