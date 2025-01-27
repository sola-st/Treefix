# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
indx = np.random.randint(65, high=122, size=7000)
x = [chr(i) for i in indx]

y, idx, count = array_ops.unique_with_counts(x)
tf_y, tf_idx, tf_count = self.evaluate([y, idx, count])

self.assertEqual(len(x), len(tf_idx))
self.assertEqual(len(tf_y), len(np.unique(x)))
for i in range(len(x)):
    self.assertEqual(x[i], tf_y[tf_idx[i]].decode('ascii'))
for value, count in zip(tf_y, tf_count):
    with self.subTest(value=value, count=count):
        v = [1 if x[i] == value.decode('ascii') else 0 for i in range(7000)]
        self.assertEqual(count, sum(v))
