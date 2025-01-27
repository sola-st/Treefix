# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    raw = [[[[[1, 2, 4, 5], [5, 6, 7, 8], [9, 10, 11, 12]]],
            [[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]]]
    checker = StridedSliceChecker(self, raw)
    # new axis (followed by implicit ellipsis)
    _ = checker[np.newaxis]
    # newaxis after ellipsis
    _ = checker[..., np.newaxis]
    # newaxis in between ellipsis and explicit range
    _ = checker[..., np.newaxis, :]
    _ = checker[:, ..., np.newaxis, :, :]
    # Reverse final dimension with new axis
    _ = checker[:, :, np.newaxis, :, 2::-1]
    # Ellipsis in middle of two newaxis
    _ = checker[np.newaxis, ..., np.newaxis]
