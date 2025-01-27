# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for dtype in STRIDED_SLICE_TYPES:
    with self.subTest(dtype=dtype):
        checker = StridedSliceAssignChecker(
            self, [[1, 2, 3], [4, 5, 6]],
            use_resource=use_resource,
            tensor_type=dtype)
        # Check if equal
        checker[:] = [[10, 20, 30], [40, 50, 60]]
        # Check trivial (1,1) shape tensor
        checker[1:2, 1:2] = [[66]]
        # shrinks shape changes
        checker[1:2, 1] = [66]
        checker[1, 1:2] = [66]
        checker[1, 1] = 66
        # newaxis shape changes
        checker[:, None, :] = [[[10, 20, 30]], [[40, 50, 50]]]
        # shrink and newaxis
        checker[None, None, 0, 0:1] = [[[99]]]
        # Non unit strides
        checker[::1, ::-2] = [[3, 33], [4, 44]]
        # degenerate interval
        checker[8:10, 0] = []
        checker[8:10, 8:10] = [[]]
    # Assign vector to scalar (rank-0) using newaxis
checker2 = StridedSliceAssignChecker(self, 222)
checker2[()] = 6  # no indices
checker2[...] = 6  # ellipsis
checker2[None] = [6]  # new axis
