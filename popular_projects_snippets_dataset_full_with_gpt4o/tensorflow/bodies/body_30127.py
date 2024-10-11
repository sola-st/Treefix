# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    scalar = np.array(0)
    # Test tensor type mask
    checker = StridedSliceChecker(self, StridedSliceChecker.REF_TENSOR)
    _ = checker[checker.x > 2]
    _ = checker[checker.x <= 5]
    _ = checker[ops.convert_to_tensor(scalar)]

    # Test numpy array type mask
    raw = np.array([[[[[1, 2, 4, 5], [5, 6, 7, 8], [9, 10, 11, 12]]],
                     [[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23,
                                                            24]]]]])
    checker1 = StridedSliceChecker(self, raw)
    _ = checker1[raw >= 4]
    _ = checker1[raw < 19]
    _ = checker1[scalar]

    # Test boolean and non boolean cases
    mask = np.array([True, False, True])
    raw1 = np.array([[1, 2, 4, 5], [5, 6, 7, 8], [9, 10, 11, 12]])
    checker2 = StridedSliceChecker(self, raw1)
    _ = checker2[mask]
    _ = checker2[ops.convert_to_tensor(mask)]
