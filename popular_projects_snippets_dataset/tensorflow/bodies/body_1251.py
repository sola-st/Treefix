# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
params = np.array(
    [[-8, -1, -2, -3, -7, -5], [8, 1, 2, 3, 7, 5]], dtype=np.float32).T
indices = np.array(
    [
        4,
    ], dtype=np.int32)
gather_nd_val = self._runGather(params, indices)
self.assertAllEqual(np.array([-7, 7]), gather_nd_val)
