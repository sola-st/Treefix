# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
x_shapes = [[20, 7, 3], [20, 3, 3], [20, 1, 3]]
output_shape = [4, 11, 3]
with self.cached_session():
    x_1 = array_ops.placeholder(dtypes.float64)
    x_2 = array_ops.placeholder(dtypes.float64)
    x_3 = array_ops.placeholder(dtypes.float64)
    xs = [x_1, x_2, x_3]

    x_concat = array_ops.concat(xs, 1)
    output = array_ops.gather(x_concat, [1, 2, 0, 5])
    params = {
        x_1: np.random.random_sample(x_shapes[0]).astype(np.float64),
        x_2: np.random.random_sample(x_shapes[1]).astype(np.float64),
        x_3: np.random.random_sample(x_shapes[2]).astype(np.float64)
    }
    err = gradient_checker.compute_gradient_error(xs, x_shapes, output,
                                                  output_shape,
                                                  extra_feed_dict=params)
self.assertLess(err, 1e-11)
