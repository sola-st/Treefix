# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    raw = [[[[[1, 2], [3, 4], [5, 6]]], [[[7, 8], [9, 10], [11, 12]]]]]
    checker = StridedSliceChecker(self, raw)

    _ = checker[0:]
    # implicit ellipsis
    _ = checker[0:, ...]
    # ellipsis alone
    _ = checker[...]
    # ellipsis at end
    _ = checker[0:1, ...]
    # ellipsis at begin
    _ = checker[..., 0:1]
    # ellipsis at middle
    _ = checker[0:1, ..., 0:1]
    # multiple ellipses not allowed
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "Multiple ellipses"):
        _ = checker[..., :, ...].eval()
