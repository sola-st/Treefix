# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        x = array_ops.placeholder(dtypes.float32)
        with g.gradient_override_map({"Identity": "BadGrad"}):
            y = array_ops.identity(x)
        bad = r"Empty gradient has wrong shape: expected \(0, 3\), got \(3, 0\)"
        with self.assertRaisesRegex(ValueError, bad):
            gradient_checker.compute_gradient(x, (0, 3), y, (0, 3))
        with self.assertRaisesRegex(ValueError, bad):
            gradient_checker.compute_gradient_error(x, (0, 3), y, (0, 3))
