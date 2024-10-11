# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
t = [[1, 2, 3], [4, 5, 6]]
paddings = [[
    1,
    1,
], [2, 2]]
self.assertAllEqual(
    np_array_ops.pad(t, paddings, 'constant'),
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 3, 0, 0], [0, 0, 4, 5, 6, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]])

self.assertAllEqual(
    np_array_ops.pad(t, paddings, 'reflect'),
    [[6, 5, 4, 5, 6, 5, 4], [3, 2, 1, 2, 3, 2, 1], [6, 5, 4, 5, 6, 5, 4],
     [3, 2, 1, 2, 3, 2, 1]])

self.assertAllEqual(
    np_array_ops.pad(t, paddings, 'symmetric'),
    [[2, 1, 1, 2, 3, 3, 2], [2, 1, 1, 2, 3, 3, 2], [5, 4, 4, 5, 6, 6, 5],
     [5, 4, 4, 5, 6, 6, 5]])
