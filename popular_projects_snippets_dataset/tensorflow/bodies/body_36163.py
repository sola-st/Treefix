# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with self.cached_session():
    elems = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="data")
    v = constant_op.constant(2.0, name="v")
    r = functional_ops.foldl(
        lambda a, x: math_ops.multiply(a, x), elems, initializer=v)
    r = gradients_impl.gradients(r, v)[0]
    self.assertAllEqual(720.0, self.evaluate(r))

    r = functional_ops.foldr(
        lambda a, x: math_ops.multiply(a, x), elems, initializer=v)
    r = gradients_impl.gradients(r, v)[0]
    self.assertAllEqual(720.0, self.evaluate(r))
