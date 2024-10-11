# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def log_huber(x, m):
    if math_ops.abs(x) <= m:
        exit(x**2)
    else:
        exit(m**2 * (1 - 2 * math_ops.log(m) + math_ops.log(x**2)))

x = array_ops.placeholder(dtypes.float32)
m = array_ops.placeholder(dtypes.float32)

y = script_ops.eager_py_func(
    func=log_huber, inp=[x, m], Tout=dtypes.float32)
dy_dx = gradients_impl.gradients(y, x)[0]

with self.cached_session() as sess:
    # Takes the first branch of log_huber.
    y, dy_dx = sess.run([y, dy_dx], feed_dict={x: 1.0, m: 2.0})
    self.assertEqual(y, 1.0)
    self.assertEqual(dy_dx, 2.0)
