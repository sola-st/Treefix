# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = constant_op.constant([1, 2, 3, 4, 5, 6], name="data")

r = functional_ops.foldl(
    lambda a, x: math_ops.multiply(math_ops.add(a, x), 2),
    elems)
self.assertAllEqual(208, self.evaluate(r))

r = functional_ops.foldl(
    lambda a, x: math_ops.multiply(math_ops.add(a, x), 2),
    elems,
    initializer=10)
self.assertAllEqual(880, self.evaluate(r))
