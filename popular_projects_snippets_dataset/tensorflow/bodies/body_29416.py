# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
x = np.random.choice([True, False], size=7000)
y, idx, count = gen_array_ops.unique_with_counts_v2(
    x, axis=np.array([], np.int32))
tf_y, tf_idx, tf_count = self.evaluate([y, idx, count])

self.assertEqual(len(x), len(tf_idx))
self.assertEqual(len(tf_y), len(np.unique(x)))
for i in range(len(x)):
    self.assertEqual(x[i], tf_y[tf_idx[i]])
for value, count in zip(tf_y, tf_count):
    self.assertEqual(count, np.sum(x == value))
