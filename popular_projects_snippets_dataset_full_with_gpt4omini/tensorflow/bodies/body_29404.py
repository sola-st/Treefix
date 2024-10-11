# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unique_op_test.py
# This test is only temporary, once V2 is used
# by default, the axis will be wrapped to allow `axis=None`.
x = np.random.randint(2, high=10, size=7000)
y, idx = gen_array_ops.unique_v2(x, axis=np.array([], np.int32))
tf_y, tf_idx = self.evaluate([y, idx])

self.assertEqual(len(x), len(tf_idx))
self.assertEqual(len(tf_y), len(np.unique(x)))
for i in range(len(x)):
    self.assertEqual(x[i], tf_y[tf_idx[i]])
