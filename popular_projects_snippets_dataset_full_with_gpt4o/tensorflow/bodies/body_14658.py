# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
x = [[1, 2, 3]]
self.assertAllEqual([[1], [2], [3]], np_array_ops.swapaxes(x, 0, 1))
self.assertAllEqual([[1], [2], [3]], np_array_ops.swapaxes(x, -2, -1))
x = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
self.assertAllEqual([[[0, 4], [2, 6]], [[1, 5], [3, 7]]],
                    np_array_ops.swapaxes(x, 0, 2))
self.assertAllEqual([[[0, 4], [2, 6]], [[1, 5], [3, 7]]],
                    np_array_ops.swapaxes(x, -3, -1))
