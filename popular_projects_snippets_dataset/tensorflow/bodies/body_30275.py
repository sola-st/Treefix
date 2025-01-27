# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
a = math_ops.cast(5, dtypes.int32)
b = math_ops.cast(6, dtypes.int32)

value = np.random.rand(11, 11)

with test_util.device(use_gpu=True):
    result = self.evaluate(array_ops.split(value, [a, b]))

self.assertAllEqual(result[0], value[0:5, :])
self.assertAllEqual(result[1], value[5:, :])
