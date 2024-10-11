# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
indx = np.random.randint(65, high=122, size=7000)
x = [chr(i) for i in indx]
y, idx = array_ops.unique(x)
tf_y, tf_idx = self.evaluate([y, idx])

self.assertEqual(len(x), len(tf_idx))
self.assertEqual(len(tf_y), len(np.unique(x)))
for i in range(len(x)):
    self.assertEqual(x[i], tf_y[tf_idx[i]].decode('ascii'))
