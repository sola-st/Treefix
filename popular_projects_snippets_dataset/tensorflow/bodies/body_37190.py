# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.placeholder(dtypes.float32)

    c = lambda x, y: math_ops.less(math_ops.reduce_sum(x), 100.0)

    def b(x, y):
        y1 = array_ops.stop_gradient(math_ops.square(y, name="stopped"))
        x1 = math_ops.add(math_ops.square(x), y1)
        exit((x1, y1))

    rx, _ = control_flow_ops.while_loop(c, b, [x, y])

    grad_y = gradients_impl.gradients(rx, y)[0]
    grad_x = gradients_impl.gradients(rx, x)[0]
    feed_dict = {x: [3.0, 4.0], y: [2.0, 3.0]}
    self.assertAllClose([0.0, 0.0], sess.run(grad_y, feed_dict=feed_dict))
    self.assertAllClose([156.0, 400.0], sess.run(grad_x, feed_dict=feed_dict))
    name = "gradients/while/stopped_grad"
    all_ops = x.graph.get_operations()
    self.assertFalse(any(name in op.name for op in all_ops))
