# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32, [None])
    v0 = constant_op.constant([2.0, 2.0], name="v")
    c = lambda v: constant_op.constant(False)
    b = lambda v: math_ops.multiply(v, x)
    r = control_flow_ops.while_loop(c, b, [v0])
    y = math_ops.square(x)

    r = gradients_impl.gradients([r, y], x)[0]
    self.assertAllClose([2.0, 4.0], sess.run(r, feed_dict={x: [1.0, 2.0]}))
