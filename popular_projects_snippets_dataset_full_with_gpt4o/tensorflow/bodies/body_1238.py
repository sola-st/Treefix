# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
for dtype in self.numeric_types:
    checker = StridedSliceAssignChecker(
        self, [[1, 2, 3], [4, 5, 6]], dtype=dtype)
    # No-op assignment
    checker[:] = [[10, 20, 30], [40, 50, 60]]
    # Checks trivial (1,1) shape tensor
    checker[1:2, 1:2] = [[66]]
    # shrink shape changes
    checker[1:2, 1] = [66]
    checker[1, 1:2] = [66]
    if dtype != dtypes.bfloat16.as_numpy_dtype:
        # TODO(b/68813416): valnp call above results in an ndarray and not a
        # number for bfloat16s.
        checker[1, 1] = 66
    # newaxis shape changes
    checker[:, None, :] = [[[10, 20, 30]], [[40, 50, 50]]]
    # shrink and newaxis
    checker[None, None, 0, 0:1] = [[[99]]]
    # Non unit strides
    checker[::1, 1::-1] = [[3, 33], [4, 44]]
    # degenerate interval
    checker[8:10, 0] = []
    checker[8:10, 8:10] = [[]]

    # Assign vector to scalar (rank-0) using newaxis
    checker2 = StridedSliceAssignChecker(self, 222, dtype=dtype)
    if dtype != dtypes.bfloat16.as_numpy_dtype:
        # TODO(b/68813416): valnp call above results in an ndarray and not a
        # number for bfloat16s.
        checker2[()] = 6  # no indices
        checker2[...] = 6  # ellipsis
    checker2[None] = [6]  # new axis
