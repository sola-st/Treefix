# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
with self.session():
    for dtype in _TEST_TYPES:
        for itype in np.int32, np.int64:
            params = np.zeros((7, 0, 0), dtype=dtype.as_numpy_dtype)
            indices = np.array([3, 4], dtype=itype)
            self.assertAllEqual(
                self.evaluate(array_ops.batch_gather(params, indices)),
                np.zeros((2, 0, 0)))
