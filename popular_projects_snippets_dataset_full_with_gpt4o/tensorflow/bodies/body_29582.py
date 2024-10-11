# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
# Verify that input shape and paddings shape can be unknown.
_ = array_ops.space_to_batch_nd(
    array_ops.placeholder(dtypes.float32),
    array_ops.placeholder(
        dtypes.int32, shape=(2,)),
    array_ops.placeholder(dtypes.int32))

# Only number of input dimensions is known.
t = array_ops.space_to_batch_nd(
    array_ops.placeholder(
        dtypes.float32, shape=(None, None, None, None)),
    array_ops.placeholder(
        dtypes.int32, shape=(2,)),
    array_ops.placeholder(dtypes.int32))
self.assertEqual(4, t.get_shape().ndims)

# Dimensions are partially known.
t = array_ops.space_to_batch_nd(
    array_ops.placeholder(
        dtypes.float32, shape=(None, None, None, 2)),
    array_ops.placeholder(
        dtypes.int32, shape=(2,)),
    array_ops.placeholder(dtypes.int32))
self.assertEqual([None, None, None, 2], t.get_shape().as_list())

# Dimensions are partially known.
t = array_ops.space_to_batch_nd(
    array_ops.placeholder(
        dtypes.float32, shape=(3, None, None, 2)), [2, 3],
    array_ops.placeholder(dtypes.int32))
self.assertEqual([3 * 2 * 3, None, None, 2], t.get_shape().as_list())

# Dimensions are partially known.
t = array_ops.space_to_batch_nd(
    array_ops.placeholder(
        dtypes.float32, shape=(3, None, 2, 2)), [2, 3], [[1, 1], [0, 1]])
self.assertEqual([3 * 2 * 3, None, 1, 2], t.get_shape().as_list())

# Dimensions are fully known.
t = array_ops.space_to_batch_nd(
    array_ops.placeholder(
        dtypes.float32, shape=(3, 2, 3, 2)), [2, 3], [[1, 1], [0, 0]])
self.assertEqual([3 * 2 * 3, 2, 1, 2], t.get_shape().as_list())
