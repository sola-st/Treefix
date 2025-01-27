# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
mean = variables.Variable(0.01)
stddev = variables.Variable(1.)
minval = variables.Variable(-1.)
maxval = variables.Variable(1.)

with self.cached_session() as sess:
    with backprop.GradientTape(persistent=True) as tape:
        samples = stateless.stateless_parameterized_truncated_normal(
            [1], [1, 2], mean, stddev, minval, maxval)

    sess.run(variables.variables_initializer([mean, stddev, minval, maxval]))
    [mean_grad, std_grad], mean_actual_grad, std_actual_grad = sess.run([
        tape.gradient(samples, [mean, stddev]),
        array_ops.ones_like(mean),
        (samples - mean) / stddev])
    self.assertAllClose(mean_grad, mean_actual_grad)
    self.assertAllClose(std_grad, std_actual_grad[0])

    try:
        import scipy.stats  # pylint:disable=g-import-not-at-top
        truncnorm = scipy.stats.truncnorm(a=-1., b=1., loc=0., scale=1.)
        samples_np, [minval_grad, maxval_grad] = sess.run([
            samples, tape.gradient(samples, [minval, maxval])])

        sample_cdf = truncnorm.cdf(samples_np)
        # These come from the implicit reparameterization trick.
        scipy_maxval_grad = np.exp(
            0.5 * (samples_np ** 2 - ((1. - 0.01) / 1.) ** 2) +
            np.log(sample_cdf))

        scipy_minval_grad = np.exp(
            0.5 * (samples_np ** 2 - ((-1. - 0.01) / 1.) ** 2) +
            np.log1p(-sample_cdf))

        self.assertAllClose(minval_grad, scipy_minval_grad[0], rtol=1e-2)
        self.assertAllClose(maxval_grad, scipy_maxval_grad[0], rtol=1e-2)

    except ImportError as e:
        tf_logging.warn("Cannot test truncated normal op: %s" % str(e))
