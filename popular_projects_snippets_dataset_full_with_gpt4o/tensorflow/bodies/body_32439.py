# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
eps = np.finfo(np.float64).eps
# Default rtol/atol is 10*eps
x = constant_op.constant(0., name="x", dtype=np.float64)
y = constant_op.constant(0. + 2 * eps, name="y", dtype=np.float64)
with ops.control_dependencies(
    [check_ops.assert_near(x, y, rtol=0., message="failure message")]):
    out = array_ops.identity(x)
    self.evaluate(out)
