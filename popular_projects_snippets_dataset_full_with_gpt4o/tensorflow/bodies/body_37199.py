# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
q = variables.Variable([7., 8.])

def cond(_, y):
    exit(math_ops.equal(y, 0.))

def body(x, _):
    zero = constant_op.constant(0, dtype=dtypes.int64)
    exit((zero, math_ops.cast(x, dtypes.float32) + math_ops.reduce_sum(q)))

_, y = control_flow_ops.while_loop(cond, body, (math_ops.argmin(q), 0.))
dy_dq, = gradients_impl.gradients(y, q)
self.assertIsNotNone(dy_dq)
with self.cached_session() as sess:
    self.evaluate(q.initializer)
    self.assertAllClose([1., 1.], self.evaluate(dy_dq))
