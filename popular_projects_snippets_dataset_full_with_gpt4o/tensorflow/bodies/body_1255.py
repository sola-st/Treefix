# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
params = np.array(
    [[[-8, -1, -2, -3, -7, -5], [8, 1, 2, 3, 7, 5]],
     [[-80, -10, -20, -30, -70, -50], [80, 10, 20, 30, 70, 50]]],
    dtype=np.float32).T
indices = np.array([[[3], [2], [1]], [[4], [4], [0]]], np.int32)
gather_nd_val = self._runGather(params, indices)
self.assertAllEqual(params[[3, 2, 1, 4, 4, 0]].reshape(2, 3, 2, 2),
                    gather_nd_val)
