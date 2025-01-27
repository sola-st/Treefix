# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
x_shapes = [[20, 7, 3], [10, 7, 3], [14, 7, 3]]
output_shape = [44, 7, 3]
x_vals = [
    np.random.random_sample(x_shape).astype(np.float64)
    for x_shape in x_shapes
]
with self.cached_session():
    xs = [constant_op.constant(x_val) for x_val in x_vals]
    output = array_ops.concat(xs, 0)
    err = gradient_checker.compute_gradient_error(xs, x_shapes, output,
                                                  output_shape)
self.assertLess(err, 1e-11)
