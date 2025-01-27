# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py

def ops_test(v1, v2):
    a = constant_op.constant(v1)
    b = constant_op.constant(v2)

    self.assertAllEqual((-a), np.negative(v1))
    self.assertAllEqual(abs(b), np.absolute(v2))

    self.assertAllEqual((a + b), np.add(v1, v2))
    self.assertAllEqual((a - b), np.subtract(v1, v2))
    self.assertAllEqual((a * b), np.multiply(v1, v2))
    self.assertAllEqual((a * a), np.multiply(v1, v1))

    if all(x >= 0 for x in v2):
        self.assertAllEqual((a**b), np.power(v1, v2))
    self.assertAllEqual((a / b), np.true_divide(v1, v2))

    self.assertAllEqual((a / a), np.true_divide(v1, v1))
    self.assertAllEqual((a % b), np.mod(v1, v2))

    self.assertAllEqual((a < b), np.less(v1, v2))
    self.assertAllEqual((a <= b), np.less_equal(v1, v2))
    self.assertAllEqual((a > b), np.greater(v1, v2))
    self.assertAllEqual((a >= b), np.greater_equal(v1, v2))

    # TODO(b/120678848): Remove the else branch once we enable
    # ops.Tensor._USE_EQUALITY by default.
    if ops.Tensor._USE_EQUALITY:
        self.assertAllEqual((a == b), np.equal(v1, v2))
        self.assertAllEqual((a != b), np.not_equal(v1, v2))
    else:
        self.assertAllEqual((a == b), np.equal(v1, v2)[0])
        self.assertAllEqual((a != b), np.not_equal(v1, v2)[0])

    self.assertAllEqual(v1[0], a[constant_op.constant(0)])

ops_test([1, 4, 8], [2, 3, 5])
ops_test([1, -4, -5], [-2, 3, -6])
