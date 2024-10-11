# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
self.maybe_skip_test(dtype)
rtol, atol = self.adjust_tolerance_for_tpu(dtype, rtol, atol)
# Test values near zero.

with self.session() as sess:
    with self.test_scope():
        x = constant_op.constant(
            np.random.uniform(
                low=np.finfo(dtype).tiny, high=1.,
                size=[NUM_SAMPLES]).astype(dtype))
        a = constant_op.constant(
            np.random.uniform(
                low=np.finfo(dtype).tiny, high=1.,
                size=[NUM_SAMPLES]).astype(dtype))
        gamma_sample_grad = gen_random_ops.random_gamma_grad(a, x)
        actual_grad = implicit_reparameterization_grad(a, x)
        gamma_sample_grad, actual_grad = sess.run(
            [gamma_sample_grad, actual_grad])
        # We do this because the ratio computed in
        # implicit_reparameterization_grad can very easily result in a NaN due
        # to the computed numerator and denominator zeroing out.
        gamma_sample_grad = gamma_sample_grad[
            ~np.logical_or(np.isnan(actual_grad), np.isinf(actual_grad))]
        actual_grad = actual_grad[
            ~np.logical_or(np.isnan(actual_grad), np.isinf(actual_grad))]
self.assertAllClose(actual_grad, gamma_sample_grad, atol=atol, rtol=rtol)
