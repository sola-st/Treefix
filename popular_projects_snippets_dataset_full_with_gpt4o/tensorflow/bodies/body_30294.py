# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
# split_dim greater than rank of input.
with self.assertRaises(ValueError):
    array_ops.split(value=[[0, 1], [2, 3]], num_or_size_splits=4, axis=2)

# split dim less than -(rank of input)
with self.assertRaises(ValueError):
    array_ops.split(value=[[0, 1], [2, 3]], num_or_size_splits=4, axis=-3)

# num_split does not evenly divide the size in split_dim.
with self.assertRaisesRegex(ValueError, "should evenly divide"):
    array_ops.split(value=[0, 1, 2, 3], num_or_size_splits=3, axis=0)

# Unknown split_dim.
splits = array_ops.split(
    value=[[0, 1, 2, 3]],
    num_or_size_splits=4,
    axis=array_ops.placeholder(dtypes.int32))
for s in splits:
    self.assertEqual([None, None], s.get_shape().as_list())

# Unknown split_dim and input shape.
splits = array_ops.split(
    value=array_ops.placeholder(dtypes.float32),
    num_or_size_splits=4,
    axis=array_ops.placeholder(dtypes.int32))
for s in splits:
    self.assertEqual(None, s.get_shape().ndims)
