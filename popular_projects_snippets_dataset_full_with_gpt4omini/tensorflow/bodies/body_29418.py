# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
x = np.random.randint(2, size=0)
y, idx, count = array_ops.unique_with_counts(x)
tf_y, tf_idx, tf_count = self.evaluate([y, idx, count])

self.assertEqual(tf_idx.shape, (0,))
self.assertEqual(tf_y.shape, (0,))
self.assertEqual(tf_count.shape, (0,))
