# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
np.testing.assert_equal(
    self._cast(
        x, dst_dtype, use_gpu=use_gpu), dst_dtype(expected))
