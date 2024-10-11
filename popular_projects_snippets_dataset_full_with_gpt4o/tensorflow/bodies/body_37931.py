# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.array([["abc", "bh"], ["c", ""]])
y = np.array([["abc", "bh"], ["def", "hi"]])
with test_util.force_cpu():
    cmp_eq = math_ops.equal(x, y)
    cmp_not_eq = math_ops.not_equal(x, y)
    values = self.evaluate([cmp_eq, cmp_not_eq])
    self.assertAllEqual([[True, True], [False, False]], values[0])
    self.assertAllEqual([[False, False], [True, True]], values[1])
