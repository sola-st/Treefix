# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
shape = (10, 20, 5, 1, 17)
params = np.random.rand(*shape).astype(np.float32)
indices = np.vstack(
    [np.random.randint(0, s, size=2000, dtype=np.int32) for s in shape]).T
indices_reshaped = indices.reshape([10, 10, 20, 5])
gather_nd_val = self._runGather(params, indices_reshaped)
expected = params[tuple(indices.T)]
self.assertAllEqual(expected.reshape([10, 10, 20]), gather_nd_val)
