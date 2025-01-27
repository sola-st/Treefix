# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = constant_op.constant(0., name="x")
y = constant_op.constant(0.1, name="y", dtype=np.float32)
with ops.control_dependencies(
    [check_ops.assert_near(x, y, atol=0.5, rtol=0.,
                           message="failure message")]):
    out = array_ops.identity(x)
    self.evaluate(out)
