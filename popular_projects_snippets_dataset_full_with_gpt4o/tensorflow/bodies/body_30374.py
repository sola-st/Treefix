# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
for dtype in _TEST_TYPES:
    for itype in np.int32, np.int64:
        # Leading axis gather.
        with self.subTest(dtype=dtype, itype=itype):
            params = np.zeros((7, 0, 0), dtype=dtype.as_numpy_dtype)
            indices = np.array([3, 4], dtype=itype)
            gather = array_ops.gather(params, indices, axis=0)
            self.assertAllEqual(gather, np.zeros((2, 0, 0)))

            # Middle axis gather.
            params = np.zeros((0, 7, 0), dtype=dtype.as_numpy_dtype)
            gather = array_ops.gather(params, indices, axis=1)
            self.assertAllEqual(gather, np.zeros((0, 2, 0)))

            # Trailing axis gather.
            params = np.zeros((0, 0, 7), dtype=dtype.as_numpy_dtype)
            gather = array_ops.gather(params, indices, axis=2)
            self.assertAllEqual(gather, np.zeros((0, 0, 2)))
