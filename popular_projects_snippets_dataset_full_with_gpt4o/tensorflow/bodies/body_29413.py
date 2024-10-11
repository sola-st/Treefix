# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
for dtype in [np.int32, np.int64]:
    with self.subTest(dtype=dtype):
        x = np.array([[1, 0, 0], [1, 0, 0], [2, 0, 0]])
        y0, idx0, count0 = gen_array_ops.unique_with_counts_v2(
            x, axis=np.array([0], dtype))
        self.assertEqual(y0.shape.rank, 2)
        tf_y0, tf_idx0, tf_count0 = self.evaluate([y0, idx0, count0])
        y1, idx1, count1 = gen_array_ops.unique_with_counts_v2(
            x, axis=np.array([1], dtype))
        self.assertEqual(y1.shape.rank, 2)
        tf_y1, tf_idx1, tf_count1 = self.evaluate([y1, idx1, count1])
        self.assertAllEqual(tf_y0, np.array([[1, 0, 0], [2, 0, 0]]))
        self.assertAllEqual(tf_idx0, np.array([0, 0, 1]))
        self.assertAllEqual(tf_count0, np.array([2, 1]))
        self.assertAllEqual(tf_y1, np.array([[1, 0], [1, 0], [2, 0]]))
        self.assertAllEqual(tf_idx1, np.array([0, 1, 1]))
        self.assertAllEqual(tf_count1, np.array([1, 2]))
