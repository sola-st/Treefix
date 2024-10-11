# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    checker = StridedSliceChecker(self, StridedSliceChecker.REF_TENSOR)
    # degenerate by offering a forward interval with a negative stride
    _ = checker[0:-1:-1, :, :]
    # degenerate with a reverse interval with a positive stride
    _ = checker[-1:0, :, :]
    # empty interval in every dimension
    _ = checker[-1:0, 2:2, 2:3:-1]
    # empty first dimension only (used to break for aligned tensors).
    checker = StridedSliceChecker(self,
                                  StridedSliceChecker.REF_TENSOR_ALIGNED)
    _ = checker[1:0]
