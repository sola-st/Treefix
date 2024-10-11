# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with ops.Graph().as_default(), ops.device('/cpu:0'):
    a = constant_op.constant(6.0, shape=[1, 1])
    b = constant_op.constant(7.0, shape=[1, 1])
    c = math_ops.matmul(a, b, name='matmul')
    with session.Session():
        result = self.evaluate(c)
        self.assertAllEqual(result, [[42.0]])
