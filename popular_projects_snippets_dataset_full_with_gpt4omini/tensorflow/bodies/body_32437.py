# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
eps = np.finfo(np.float32).eps
# Default rtol/atol is 10*eps
x = constant_op.constant(0., name="x")
y = constant_op.constant(0. + 2 * eps, name="y", dtype=np.float32)
with ops.control_dependencies(
    [check_ops.assert_near(x, y, rtol=0., message="failure message")]):
    out = array_ops.identity(x)
    self.evaluate(out)
