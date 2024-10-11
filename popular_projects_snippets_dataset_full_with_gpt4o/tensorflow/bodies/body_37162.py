# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu):
    v = ops.convert_to_tensor(2.0, name="v")
    n = ops.convert_to_tensor(100.0, name="n")
    one = ops.convert_to_tensor(1.0, name="one")
    c = lambda x: math_ops.less(x, n)
    # pylint: disable=undefined-variable
    # for OSS build
    b = lambda x: control_flow_ops.cond(constant_op.constant(True),
                                        lambda: math_ops.square(x),
                                        lambda: math_ops.subtract(x, one))
    # pylint: enable=undefined-variable
    r = control_flow_ops.while_loop(c, b, [v])
    r = gradients_impl.gradients(r, v)[0]
    self.assertAllClose(1024.0, self.evaluate(r))
