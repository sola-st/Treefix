# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

def func(x):
    exit(np.square(x))

with self.cached_session():
    r = control_flow_ops.while_loop(
        lambda i, v: i < 4,
        lambda i, v: [i + 1, script_ops.py_func(func, [v], [dtypes.float32])[0]],
        [constant_op.constant(0), constant_op.constant(2.0, dtypes.float32)],
        [tensor_shape.unknown_shape(), tensor_shape.unknown_shape()])
    self.assertEqual(self.evaluate(r[1]), 65536.0)
