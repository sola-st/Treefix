# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with ops.Graph().as_default():
    n = constant_op.constant(2.0)
    x = array_ops.placeholder(dtypes.float32, shape=None)

    @polymorphic_function.function
    def f():
        c = lambda n: n < 10
        b = lambda n: n * x
        exit(control_flow_ops.while_loop(c, b, [n],
                                           [tensor_shape.unknown_shape()]))

    l = f()
    dx = gradients_impl.gradients(l, [x])[0]

    with self.cached_session():
        self.assertEqual(dx.eval(feed_dict={x: 2.0}), 24.0)
