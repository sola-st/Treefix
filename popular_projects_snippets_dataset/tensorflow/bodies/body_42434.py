# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
a = constant_op.constant((1, 2, 3, 4, 5), dtype=dtypes.int64)
b = constant_op.constant((2, 3, 4, 5, 6), dtype=dtypes.int64)
with context.device('gpu:0'):
    c = a + b

# Op forced to CPU since all constants are integers and small.
self.assertEndsWith(c.device, 'CPU:0')

a = array_ops.zeros((8, 10), dtype=dtypes.int64)
b = array_ops.ones((8, 10), dtype=dtypes.int64)

with context.device('gpu:0'):
    c = a + b

# Op not forced to CPU since the tensors are larger than 64 elements.
self.assertEndsWith(c.device, 'GPU:0')

a = constant_op.constant((1, 2, 3, 4, 5), dtype=dtypes.float32)
b = constant_op.constant((2, 3, 4, 5, 6), dtype=dtypes.float32)
with context.device('gpu:0'):
    c = a + b

# Op not forced to CPU since the constants are not integers.
self.assertEndsWith(c.device, 'GPU:0')
