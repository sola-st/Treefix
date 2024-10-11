# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
with self.session():
    params = np.ones((3, 3), dtype=np.float32)

    indices_empty = np.empty((0, 2), dtype=np.int32)
    gather_nd_ok_val = self._runGather(params, indices_empty)
    self.assertAllClose(np.empty((0,), dtype=np.float32), gather_nd_ok_val)

    indices_empty = np.empty((0, 1), dtype=np.int32)
    gather_nd_ok_val = self._runGather(params, indices_empty)
    self.assertAllClose(np.empty((0, 3), dtype=np.float32), gather_nd_ok_val)

    params_empty = np.empty((0, 3), dtype=np.float32)
    indices_empty = np.empty((0, 2), dtype=np.int32)
    gather_nd_ok_val = self._runGather(params_empty, indices_empty)
    self.assertAllClose(np.empty((0,), dtype=np.float32), gather_nd_ok_val)

    params_empty = np.empty((0, 3), dtype=np.float32)
    indices_nonempty = np.zeros((1, 2), dtype=np.int32)
    with self.assertRaisesWithPredicateMatch(
        errors.InvalidArgumentError, r"Gather dimension 0 is of size zero"):
        self._runGather(params_empty, indices_nonempty)
