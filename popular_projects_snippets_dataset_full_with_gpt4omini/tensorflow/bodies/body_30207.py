# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.cached_session():
    for dtype in [dtypes.int32, dtypes.int64]:
        with self.subTest(dtype=dtype):
            indices_1 = constant_op.constant(1621, dtype=dtype)
            dims_1 = constant_op.constant([6, 7, 8, 9], dtype=dtype)
            out_1 = array_ops.unravel_index(indices_1, dims_1)
            self.assertAllEqual(out_1, [3, 1, 4, 1])

            indices_2 = constant_op.constant([1621], dtype=dtype)
            dims_2 = constant_op.constant([6, 7, 8, 9], dtype=dtype)
            out_2 = array_ops.unravel_index(indices_2, dims_2)
            self.assertAllEqual(out_2, [[3], [1], [4], [1]])

            indices_3 = constant_op.constant([22, 41, 37], dtype=dtype)
            dims_3 = constant_op.constant([7, 6], dtype=dtype)
            out_3 = array_ops.unravel_index(indices_3, dims_3)
            self.assertAllEqual(out_3, [[3, 6, 6], [4, 5, 1]])
