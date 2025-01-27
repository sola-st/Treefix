# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
"""CheckNumericsV2 op distinguishes - & + infs when nan is present."""
with self.session(graph=ops.Graph()):
    t1 = constant_op.constant([-1.0, 1.0, 0.0])
    t2 = constant_op.constant([0.0, 0.0, 0.0])
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        r"pass through test.*had -Inf, \+Inf, and NaN values"):
        self.evaluate(
            array_ops.check_numerics_v2(t1 / t2, message="pass through test"))
