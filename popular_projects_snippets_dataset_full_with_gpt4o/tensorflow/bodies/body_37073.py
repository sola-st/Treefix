# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = array_ops.placeholder(dtypes.float32, shape=[None])
    v = constant_op.constant([2.0], name="v")
    n = constant_op.constant(0, name="n")
    c = lambda i, v: math_ops.less(i, 5)
    b = lambda i, v: [i + 1, math_ops.multiply(x, v)]
    r = control_flow_ops.while_loop(
        c,
        b, [n, v],
        [n.get_shape(), tensor_shape.unknown_shape()],
        parallel_iterations=1)

    r = gradients_impl.gradients(r[1], x)[0]
    self.assertEqual([None], r.get_shape().as_list())
    self.assertAllClose([810.0, 2560.0], r.eval(feed_dict={x: [3.0, 4.0]}))
