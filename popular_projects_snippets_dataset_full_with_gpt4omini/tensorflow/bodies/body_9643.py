# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = constant_op.constant(1.0, shape=[1, 2])
    p = variables.Variable(a, name='testExtendWithGroupBy_p')
    a_val = self.evaluate(a)  # Force an Extend after this op.
    self.assertAllEqual([[1.0, 1.0]], a_val)

    b = constant_op.constant(2.0, shape=[1, 2])
    q = variables.Variable(b, name='testExtendWithGroupBy_q')
    # Extend will happen here.
    init = control_flow_ops.group(p.initializer, q.initializer)
    s.run(init)
    p_val, q_val = s.run([p, q])

    self.assertAllEqual([[1.0, 1.0]], p_val)
    self.assertAllEqual([[2.0, 2.0]], q_val)
