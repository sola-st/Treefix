# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
with self.cached_session():
    inx = constant_op.constant(np_input.tolist())
    xs = list(np_input.shape)
    y = manip_ops.roll(inx, shift, axis)
    # Expected y's shape to be the same
    ys = xs
    jacob_t, jacob_n = gradient_checker.compute_gradient(
        inx, xs, y, ys, x_init_value=np_input)
    self.assertAllClose(jacob_t, jacob_n, rtol=1e-5, atol=1e-5)
