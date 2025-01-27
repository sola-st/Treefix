# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for dtype in STRIDED_SLICE_TYPES:
    with self.subTest(dtype=dtype):
        checker = StridedSliceAssignChecker(
            self, [[1, 2, 3], [4, 5, 6]],
            use_resource=use_resource,
            tensor_type=dtype)
        # Broadcast to full LHS.
        checker[:] = [[40, 50, 60]]
        # Assign a trivial (1,1) tensor.
        checker[1:2, 1:2] = 66
        # Broadcast with shrink axis shape changes.
        checker[1:2, 1] = 66
        checker[1, 1:2] = 66
        # Broadcast with newaxis shape changes.
        checker[:, None, :] = [10, 20, 30]
        # Broadcast with both shrink and newaxis.
        checker[None, None, 0, 0:1] = 99
        # Broadcast with non-unit strides.
        checker[::1, ::-2] = [[4, 44]]
        # Broadcast a degenerate interval.
        checker[8:10, 8:10] = []
