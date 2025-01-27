# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
ctx = context.context()
is_eager = ctx is not None and ctx.executing_eagerly()
if test.is_gpu_available(cuda_only=True) or \
      (test_util.IsMklEnabled() and is_eager is False):
    self._VerifyDilatedConvValues(
        tensor_in_sizes=[1, 4, 6, 3, 1],
        filter_in_sizes=[2, 2, 2, 1, 1],
        stride=1,
        padding="VALID",
        dilations=[1, 2, 1])
