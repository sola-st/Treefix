# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
x = np.random.randint(2, size=0)
y, idx = array_ops.unique(x)
tf_y, tf_idx = self.evaluate([y, idx])

self.assertEqual(len(x), len(tf_idx))
self.assertEqual(len(tf_y), len(np.unique(x)))
