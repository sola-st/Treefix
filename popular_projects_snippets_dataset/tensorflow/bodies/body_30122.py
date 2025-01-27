# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    raw = [[[[[1, 2, 4, 5], [5, 6, 7, 8], [9, 10, 11, 12]]],
            [[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]]]
    checker = StridedSliceChecker(self, raw, check_type_infer=False)
    bar = constant_op.constant(2)
    bar2 = constant_op.constant(3)
    _ = checker[..., bar:bar2]
    _ = checker[..., bar]
    _ = checker[..., 3]
    _ = checker[..., 2**64 // 2**63]  # Test longs in Python 2
