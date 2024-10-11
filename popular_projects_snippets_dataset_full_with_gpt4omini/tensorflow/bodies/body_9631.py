# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = constant_op.constant(1.0, shape=[1, 2])
    v = variables.Variable(a, name='testFetchOperationObject_v')
    s.run(v.initializer)
    v_val = s.run(v)
    self.assertAllEqual([[1.0, 1.0]], v_val)
