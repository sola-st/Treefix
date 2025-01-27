# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[1, 2], name='b')
    v = variables.VariableV1(a, a.dtype)
    assign_a_to_v = state_ops.assign(v, a)

    self.evaluate(assign_a_to_v)

    v_val = self.evaluate(v)
    self.assertAllEqual([[1.0, 1.0]], v_val)

    assign_b_to_v = state_ops.assign(v, b)

    self.evaluate(assign_b_to_v)
    v_val = self.evaluate(v)
    self.assertAllEqual([[2.0, 2.0]], v_val)

    assign_b_to_v.eval(feed_dict={'b:0': [[3.0, 3.0]]})
    v_val = self.evaluate(v)
    self.assertAllEqual([[3.0, 3.0]], v_val)
