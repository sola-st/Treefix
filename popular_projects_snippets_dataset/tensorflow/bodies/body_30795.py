# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/betainc_op_test.py
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    np_dt = dtype.as_numpy_dtype

    # Test random values
    a_s = a_s.astype(np_dt)  # in (0, infty)
    b_s = b_s.astype(np_dt)  # in (0, infty)
    x_s = x_s.astype(np_dt)  # in (0, 1)
    tf_a_s = constant_op.constant(a_s, dtype=dtype)
    tf_b_s = constant_op.constant(b_s, dtype=dtype)
    tf_x_s = constant_op.constant(x_s, dtype=dtype)
    tf_out_t = math_ops.betainc(tf_a_s, tf_b_s, tf_x_s)
    with self.cached_session():
        tf_out = self.evaluate(tf_out_t)
    scipy_out = special.betainc(a_s, b_s, x_s, dtype=np_dt)

    # the scipy version of betainc uses a double-only implementation.
    # TODO(ebrevdo): identify reasons for (sometime) precision loss
    # with doubles
    rtol = 1e-4
    atol = 1e-5
    self.assertAllCloseAccordingToType(
        scipy_out, tf_out, rtol=rtol, atol=atol)

    # Test out-of-range values (most should return nan output)
    combinations = list(itertools.product([-1, 0, 0.5, 1.0, 1.5], repeat=3))
    a_comb, b_comb, x_comb = np.asarray(list(zip(*combinations)), dtype=np_dt)
    with self.cached_session():
        tf_comb = math_ops.betainc(a_comb, b_comb, x_comb).eval()
    scipy_comb = special.betainc(a_comb, b_comb, x_comb, dtype=np_dt)
    self.assertAllCloseAccordingToType(
        scipy_comb, tf_comb, rtol=rtol, atol=atol)

    # Test broadcasting between scalars and other shapes
    with self.cached_session():
        self.assertAllCloseAccordingToType(
            special.betainc(0.1, b_s, x_s, dtype=np_dt),
            math_ops.betainc(0.1, b_s, x_s).eval(),
            rtol=rtol,
            atol=atol)
        self.assertAllCloseAccordingToType(
            special.betainc(a_s, 0.1, x_s, dtype=np_dt),
            math_ops.betainc(a_s, 0.1, x_s).eval(),
            rtol=rtol,
            atol=atol)
        self.assertAllCloseAccordingToType(
            special.betainc(a_s, b_s, 0.1, dtype=np_dt),
            math_ops.betainc(a_s, b_s, 0.1).eval(),
            rtol=rtol,
            atol=atol)
        self.assertAllCloseAccordingToType(
            special.betainc(0.1, b_s, 0.1, dtype=np_dt),
            math_ops.betainc(0.1, b_s, 0.1).eval(),
            rtol=rtol,
            atol=atol)
        self.assertAllCloseAccordingToType(
            special.betainc(0.1, 0.1, 0.1, dtype=np_dt),
            math_ops.betainc(0.1, 0.1, 0.1).eval(),
            rtol=rtol,
            atol=atol)

    with self.assertRaisesRegex(ValueError, "must be equal"):
        math_ops.betainc(0.5, [0.5], [[0.5]])

    with self.cached_session():
        with self.assertRaisesOpError("Shapes of .* are inconsistent"):
            a_p = array_ops.placeholder(dtype)
            b_p = array_ops.placeholder(dtype)
            x_p = array_ops.placeholder(dtype)
            math_ops.betainc(a_p, b_p, x_p).eval(
                feed_dict={a_p: 0.5,
                           b_p: [0.5],
                           x_p: [[0.5]]})

except ImportError as e:
    tf_logging.warn("Cannot test special functions: %s" % str(e))
