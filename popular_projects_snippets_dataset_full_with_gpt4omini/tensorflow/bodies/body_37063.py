# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
run_options = config_pb2.RunOptions(timeout_in_ms=1)
with self.cached_session() as sess:
    n = constant_op.constant(0)
    c = lambda x: True
    b = lambda x: math_ops.add(x, 1)
    r = control_flow_ops.while_loop(c, b, [n])
    with self.assertRaises(errors_impl.DeadlineExceededError):
        sess.run(r, options=run_options)
