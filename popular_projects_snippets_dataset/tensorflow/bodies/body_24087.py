# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
self.session_root = tempfile.mkdtemp()

self.v = variables.VariableV1(10.0, dtype=dtypes.float32, name="v")
self.delta = constant_op.constant(1.0, dtype=dtypes.float32, name="delta")
self.eta = constant_op.constant(-1.4, dtype=dtypes.float32, name="eta")
self.inc_v = state_ops.assign_add(self.v, self.delta, name="inc_v")
self.dec_v = state_ops.assign_add(self.v, self.eta, name="dec_v")

self.ph = array_ops.placeholder(dtypes.float32, shape=(), name="ph")
self.inc_w_ph = state_ops.assign_add(self.v, self.ph, name="inc_w_ph")

self.sess = session.Session()
self.sess.run(self.v.initializer)
