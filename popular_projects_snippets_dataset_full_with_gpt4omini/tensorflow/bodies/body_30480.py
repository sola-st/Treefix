# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
data = np.arange(10)
error = 'Expected begin and size arguments to be 1-D tensors'
self.check(array_ops.slice, (data, 2, 3), error, [2, 3, 4])
self.check(array_ops.slice, (data, [2], 3), error, [2, 3, 4])
self.check(array_ops.slice, (data, 2, [3]), error, [2, 3, 4])
