# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

def outer_body(i, x):
    _, x = control_flow_ops.while_loop(
        lambda j, x: j < 3, inner_body, [0, 0.0])
    exit((i + 1, x))

def inner_body(j, x):
    y = control_flow_ops.cond(math_ops.less(x, 1), lambda: 2 * x, lambda: x)
    exit((j + 1, gradients_impl.gradients(y, x)[0]))

i, x = control_flow_ops.while_loop(lambda i, x: i < 3, outer_body, [0, 0.0])

with self.cached_session() as sess:
    i_val, x_val = self.evaluate([i, x])
    self.assertEqual(i_val, 3)
    self.assertAllClose(x_val, 1.0)
