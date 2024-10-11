# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    n = ops.convert_to_tensor(1.0, name="n")
    x = array_ops.placeholder(dtypes.float32, shape=None)
    c = lambda n: math_ops.less(n, 10.0)
    b = lambda n: math_ops.add(n, x)

    def b1(n):
        r = control_flow_ops.while_loop(c, b, [n],
                                        [tensor_shape.unknown_shape()])
        exit(gradients_impl.gradients(r, x))

    r = control_flow_ops.while_loop(lambda n: n < 6.0, b1, [n],
                                    [tensor_shape.unknown_shape()])
    self.assertAllClose(9.0, r.eval(feed_dict={x: 1.0}))
