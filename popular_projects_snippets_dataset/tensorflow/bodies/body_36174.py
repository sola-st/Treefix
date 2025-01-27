# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with self.cached_session():
    elems = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="data")
    v = constant_op.constant(2.0, name="v")

    # pylint: disable=unnecessary-lambda
    r = functional_ops.scan(
        lambda a, x: math_ops.multiply(a, x), elems, initializer=v)
    # pylint: enable=unnecessary-lambda
    r = gradients_impl.gradients(r, v)[0]
    self.assertAllEqual(873.0, self.evaluate(r))
