# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu) as sess:
    a = constant_op.constant(3.0, name="a")
    v = constant_op.constant(2.0, name="v")
    c = lambda v: math_ops.less(v, 100.0)
    b = lambda v: math_ops.multiply(v, a)
    r = control_flow_ops.while_loop(c, b, [v], parallel_iterations=p_iters)

    grad_a, grad_v = gradients_impl.gradients(r, [a, v])
    grad_a_val, grad_v_val = self.evaluate([grad_a, grad_v])
    self.assertAllClose(216.0, grad_a_val)
    self.assertAllClose(81.0, grad_v_val)
