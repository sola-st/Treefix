# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
a = [4, 3, 5, 7, 6, 8]
indices = [0, 1, 4]
self.assertAllEqual([4, 3, 6], np_array_ops.take(a, indices))
indices = [[0, 1], [2, 3]]
self.assertAllEqual([[4, 3], [5, 7]], np_array_ops.take(a, indices))
a = [[4, 3, 5], [7, 6, 8]]
self.assertAllEqual([[4, 3], [5, 7]], np_array_ops.take(a, indices))
a = np.random.rand(2, 16, 3)
axis = 1
self.assertAllEqual(
    np.take(a, indices, axis=axis),
    np_array_ops.take(a, indices, axis=axis))
