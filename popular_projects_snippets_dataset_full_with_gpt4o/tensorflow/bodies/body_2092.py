# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
start = array_ops.placeholder(np.int32, shape=(2, 3, 4))

# If slice_sizes are known, the operand shape does not matter.
# The shape of the output is equal to slice_sizes.
slice_sizes = np.array([1, 2, 4], dtype=np.int32)
for a_shape in [(2, 3, 4), (None, 3, 4), None]:
    a = array_ops.placeholder(np.float32, shape=a_shape)
    res = xla.dynamic_slice(a, start, slice_sizes)
    self.assertEqual(res.shape.as_list(), [1, 2, 4])

# The first two dimension slice sizes are known
slice_sizes = array_ops.stack([1, 2, array_ops.placeholder(np.int32, [])])
for a_shape in [(2, 3, 4), (None, 3, 4), None]:
    a = array_ops.placeholder(np.float32, shape=a_shape)
    res = xla.dynamic_slice(a, start, slice_sizes)
    self.assertEqual(res.shape.as_list(), [1, 2, None])

# If slice_sizes has known rank and dimension, but is not a constant
# then output has the same rank, but with unknown dimensions.
slice_sizes = array_ops.placeholder(np.int32, [3])
for a_shape in [(2, 3, 4), (None, 3, 4), None]:
    a = array_ops.placeholder(np.float32, shape=a_shape)
    res = xla.dynamic_slice(a, start, slice_sizes)
    self.assertEqual(res.shape.as_list(), [None, None, None])

# slice sizes has known rank, but unknown dimensions.
# then the output has the same rank as the operand, but with unknown
# dimensions.
slice_sizes = array_ops.placeholder(np.int32, [None])
for a_shape in [(2, 3, 4), (None, 3, 4)]:
    a = array_ops.placeholder(np.float32, shape=a_shape)
    res = xla.dynamic_slice(a, start, slice_sizes)
    self.assertEqual(res.shape.as_list(), [None, None, None])

a = array_ops.placeholder(np.float32, shape=None)
slice_sizes = array_ops.placeholder(np.int32, [None])
res = xla.dynamic_slice(a, start, slice_sizes)
self.assertIsNone(res.shape.rank)
