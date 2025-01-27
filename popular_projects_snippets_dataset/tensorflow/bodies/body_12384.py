# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        x = array_ops.placeholder(dtypes.float32)
        with g.gradient_override_map({"Identity": "NaNGrad"}):
            y = array_ops.identity(x)
            error = gradient_checker.compute_gradient_error(x, (), y, ())
            # Typical test would assert error < max_err, so assert this test would
            # raise AssertionError, since NaN is not < 1.0.
            with self.assertRaisesRegex(AssertionError, "False is not true"):
                self.assertTrue(error < 1.0)
