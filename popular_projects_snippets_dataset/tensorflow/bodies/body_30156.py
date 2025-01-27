# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
original_dy = array_ops.reshape(
    math_ops.cast(math_ops.range(1, 5, 1), dtypes.float32), shape=(4, 1, 1))
original_shape = constant_op.constant([6, 4, 4], dtype=dtypes.int64)
begin = constant_op.constant([0, 0, 0], dtype=dtypes.int64)
end = constant_op.constant([4, 1, 1], dtype=dtypes.int64)
strides = constant_op.constant([1, 1, 1], dtype=dtypes.int64)
dx = array_ops.strided_slice_grad(original_shape, begin, end, strides,
                                  original_dy)
self.evaluate(dx)
