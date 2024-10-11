# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
params = np.array(
    [[[-8, -1, -2, -3, -7, -5], [8, 1, 2, 3, 7, 5]],
     [[-80, -10, -20, -30, -70, -50], [80, 10, 20, 30, 70, 50]]],
    dtype=np.float32).T
indices = np.array([[], []], dtype=np.int32)  # Size (2, 0)
gather_nd_val = self._runGather(params, indices)
self.assertAllEqual(
    np.vstack((params[np.newaxis, :], params[np.newaxis, :])),
    gather_nd_val)
