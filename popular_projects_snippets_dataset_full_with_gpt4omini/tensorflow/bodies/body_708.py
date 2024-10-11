# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
self.maybe_skip_test(dtype)
with self.session():
    with self.test_scope():
        x = constant_op.constant(
            np.random.uniform(low=1., high=100.,
                              size=[NUM_SAMPLES]).astype(dtype))
        a = constant_op.constant(
            np.random.uniform(low=1., high=100.,
                              size=[NUM_SAMPLES]).astype(dtype))

        f = lambda b: _igamma(b, x)
        max_error = gradient_checker_v2.max_error(
            *gradient_checker_v2.compute_gradient(f, x=[a], delta=1e-3))
self.assertLessEqual(max_error, tolerance)
