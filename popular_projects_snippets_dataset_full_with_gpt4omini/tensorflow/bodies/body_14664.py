# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
x = np_array_ops.arange(9)
y = np_array_ops.split(x, 3)
self.assertListEqual([([0, 1, 2]), ([3, 4, 5]), ([6, 7, 8])], y)

x = np_array_ops.arange(8)
y = np_array_ops.split(x, [3, 5, 6, 10])
self.assertListEqual([([0, 1, 2]), ([3, 4]), ([5]), ([6, 7]), ([])], y)
