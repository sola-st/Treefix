# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [20, 7, 3]
np.random.seed(1)
x_np = np.random.random_sample(x_shape).astype(np.float64)
with self.cached_session():
    x_tf = constant_op.constant(x_np, name="x")
    # TODO(b/241834841): Test l2_normalize with `axis` set to other dims
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        nn_impl.l2_normalize, [x_tf])
    self.assertAllClose(theoretical, numerical)
