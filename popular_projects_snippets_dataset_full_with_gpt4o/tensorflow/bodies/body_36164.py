# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="data")
v = constant_op.constant(2.0, name="v")

# pylint: disable=unnecessary-lambda
r = functional_ops.scan(lambda a, x: math_ops.multiply(a, x), elems)
self.assertAllEqual([1., 2., 6., 24., 120., 720.], self.evaluate(r))

r = functional_ops.scan(
    lambda a, x: math_ops.multiply(a, x), elems, initializer=v)
self.assertAllEqual([2., 4., 12., 48., 240., 1440.], self.evaluate(r))
