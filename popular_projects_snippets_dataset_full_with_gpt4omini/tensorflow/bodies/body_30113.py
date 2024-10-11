# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

with test_util.force_gpu():
    x = constant_op.constant([1., 2., 3.])
    begin = constant_op.constant([2], dtype=dtypes.int64)
    end = constant_op.constant([3], dtype=dtypes.int64)
    strides = constant_op.constant([1], dtype=dtypes.int64)
    s = array_ops.strided_slice(x, begin, end, strides)
    self.assertAllEqual([3.], self.evaluate(s))
