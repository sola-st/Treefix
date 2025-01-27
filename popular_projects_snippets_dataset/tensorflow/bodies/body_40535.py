# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
three = constant_op.constant(3.0)
almost_three = constant_op.constant(2.8)
almost_equal = math_ops.approximate_equal(
    three, almost_three, tolerance=0.3)
self.assertTrue(almost_equal)
