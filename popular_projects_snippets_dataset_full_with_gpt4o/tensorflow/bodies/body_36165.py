# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = constant_op.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], name="data")
v = constant_op.constant(2.0, name="v")

# pylint: disable=unnecessary-lambda
r = functional_ops.scan(lambda a, x: math_ops.multiply(a, x), elems,
                        reverse=True)
self.assertAllEqual([720., 720., 360., 120., 30., 6.], self.evaluate(r))
r = functional_ops.scan(
    lambda a, x: math_ops.multiply(a, x), elems, initializer=v,
    reverse=True)
self.assertAllEqual([1440., 1440., 720., 240., 60., 12.],
                    self.evaluate(r))
