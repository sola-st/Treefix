# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[2, 3])
    c = math_ops.matmul(a, b)
    v = variables.Variable(c, name='testExtendWithStatefulOperations_v')
    v.initializer.run()
    v_val = self.evaluate(v)
    self.assertAllEqual([[4.0, 4.0, 4.0]], v_val)
    d = constant_op.constant(3.0, shape=[2, 3])
    e = math_ops.matmul(a, d)
    assign_e_to_v = state_ops.assign(v, e)
    # Extend will happen here.
    e_val = self.evaluate(e)
    self.assertAllEqual([[6.0, 6.0, 6.0]], e_val)
    v_val = self.evaluate(v)
    self.assertAllEqual([[4.0, 4.0, 4.0]], v_val)
    s.run(assign_e_to_v)
    v_val = self.evaluate(v)
    self.assertAllEqual([[6.0, 6.0, 6.0]], v_val)
