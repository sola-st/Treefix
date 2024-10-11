# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    self.assertEqual(ops.get_default_graph(), s.graph)
    a = constant_op.constant(1.0, shape=[1, 2])
    b = constant_op.constant(2.0, shape=[2, 3])
    c = math_ops.matmul(a, b)
    v = variables.Variable(c, name='var_%d' % i)

    # Block here until all threads have constructed their graph.
    constructed_event.set()
    continue_event.wait()

    assign_c_to_v = state_ops.assign(v, c)
    v.initializer.run()
    self.evaluate(assign_c_to_v)
    v_val = self.evaluate(v)
    self.assertAllEqual([[4.0, 4.0, 4.0]], v_val)
    d = constant_op.constant(3.0, shape=[2, 3])
    e = math_ops.matmul(a, d)
    assign_e_to_v = state_ops.assign(v, e)
    e_val = self.evaluate(e)
    self.assertAllEqual([[6.0, 6.0, 6.0]], e_val)
    v_val = self.evaluate(v)
    self.assertAllEqual([[4.0, 4.0, 4.0]], v_val)
    s.run(assign_e_to_v)
    v_val = self.evaluate(v)
    self.assertAllEqual([[6.0, 6.0, 6.0]], v_val)
    self.assertEqual(ops.get_default_graph(), s.graph)
