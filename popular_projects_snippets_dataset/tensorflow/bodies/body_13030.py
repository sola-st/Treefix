# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_np = np.random.randn(*x_shape).astype(np.float64)
x_tf = constant_op.constant(x_np)
theoretical, numerical = gradient_checker_v2.compute_gradient(
    nn_ops.softmax_v2, [x_tf])
self.assertAllClose(theoretical, numerical)
