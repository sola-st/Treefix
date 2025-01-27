# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
x = np.array([3, 5, 3, 4, 1, 4, 9, 8, 6, 3, 5, 7, 8, 8, 4, 6, 4, 2, 5, 6])
true_y = np.array([3, 5, 4, 1, 9, 8, 6, 7, 2])
true_idx = np.array(
    [0, 1, 0, 2, 3, 2, 4, 5, 6, 0, 1, 7, 5, 5, 2, 6, 2, 8, 1, 6])
true_count = np.array([3, 3, 4, 1, 1, 3, 3, 1, 1])
y, idx, count = array_ops.unique_with_counts(x)
tf_y, tf_idx, tf_count = self.evaluate([y, idx, count])
self.assertAllEqual(tf_y, true_y)
self.assertAllEqual(tf_idx, true_idx)
self.assertAllEqual(tf_count, true_count)
