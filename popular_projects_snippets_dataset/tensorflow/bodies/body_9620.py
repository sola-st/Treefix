# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    a = constant_op.constant(42.0)
    b = control_flow_ops.no_op()  # An op, not a tensor.
    c = constant_op.constant(44.0)
    v = variables.Variable([54.0])
    assign = v.assign([63.0])
    res = sess.run([a, b, c, a.name, assign.op])
    self.assertIsInstance(res, list)
    self.assertEqual([42.0, None, 44.0, 42.0, None], res)
    list_runner = sess.make_callable([a, b, c, a.name, assign.op])
    res = list_runner()
    self.assertIsInstance(res, list)
    self.assertEqual([42.0, None, 44.0, 42.0, None], res)
