# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
for unsigned_type in (dtypes.uint32, dtypes.uint64):
    with self.subTest(unsigned_type=unsigned_type):
        params = self._buildParams(
            np.array([[1, 2, 3], [7, 8, 9]]), unsigned_type)
        with self.cached_session():
            self.assertAllEqual([7, 8, 9], array_ops.gather(params, 1, axis=0))
            self.assertAllEqual([1, 7], array_ops.gather(params, 0, axis=1))
