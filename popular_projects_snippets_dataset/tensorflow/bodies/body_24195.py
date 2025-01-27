# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
self._observer = {
    "sess_init_count": 0,
    "request_sess": None,
    "on_run_start_count": 0,
    "run_fetches": None,
    "run_feed_dict": None,
    "on_run_end_count": 0,
    "performed_action": None,
    "tf_error": None,
}

self._dump_root = tempfile.mkdtemp()

self._sess = session.Session(config=self._no_rewrite_session_config())

self._a_init_val = np.array([[5.0, 3.0], [-1.0, 0.0]])
self._b_init_val = np.array([[2.0], [-1.0]])
self._c_val = np.array([[-4.0], [6.0]])

self._a_init = constant_op.constant(
    self._a_init_val, shape=[2, 2], name="a_init")
self._b_init = constant_op.constant(
    self._b_init_val, shape=[2, 1], name="b_init")

self._ph = array_ops.placeholder(dtype=dtypes.float64, name="ph")

self._a = variables.Variable(self._a_init, name="a1")
self._b = variables.Variable(self._b_init, name="b")
self._c = constant_op.constant(self._c_val, shape=[2, 1], name="c")

# Matrix product of a and b.
self._p = math_ops.matmul(self._a, self._b, name="p1")

# Matrix product of a and ph.
self._q = math_ops.matmul(self._a, self._ph, name="q")

# Sum of two vectors.
self._s = math_ops.add(self._p, self._c, name="s")

# Initialize the variables.
self._sess.run(self._a.initializer)
self._sess.run(self._b.initializer)
