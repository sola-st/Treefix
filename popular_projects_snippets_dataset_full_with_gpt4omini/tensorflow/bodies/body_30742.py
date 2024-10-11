# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
x_shapes = [[20, 7, 3], [20, 3, 3], [20, 1, 3]]
output_shape = [4, 11, 3]
x_vals = [
    np.random.random_sample(x_shape).astype(np.float64)
    for x_shape in x_shapes
]
with self.cached_session():
    xs = [constant_op.constant(x_val) for x_val in x_vals]
    x_concat = array_ops.concat(xs, 1)
    output = array_ops.gather(x_concat, [1, 2, 0, 5])
    err = gradient_checker.compute_gradient_error(xs, x_shapes, output,
                                                  output_shape)
self.assertLess(err, 1e-11)
