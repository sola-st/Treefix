# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
dtypes = [np.float16, np.float32, np.float64, np.int64, np.int32,
          np.complex64, np.complex128]
with self.session():
    for dtype in dtypes:
        for itype in (np.int32, np.int64):
            data = np.zeros((2, 0), dtype=dtype)
            segment_ids = np.array([0, 1], dtype=itype)
            unsorted = math_ops.unsorted_segment_sum(data, segment_ids, 2)
            self.assertAllEqual(unsorted, np.zeros((2, 0), dtype=dtype))
