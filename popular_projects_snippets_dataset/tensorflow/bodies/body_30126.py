# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    checker = StridedSliceChecker(self,
                                  StridedSliceChecker.REF_TENSOR_ALIGNED)
    # Identity
    _ = checker[:]
    # Identity
    _ = checker[...]
    # Identity
    _ = checker[np.newaxis, ..., np.newaxis]
    # First axis slice
    _ = checker[1:]
    # First axis slice
    _ = checker[np.newaxis, 1:]
