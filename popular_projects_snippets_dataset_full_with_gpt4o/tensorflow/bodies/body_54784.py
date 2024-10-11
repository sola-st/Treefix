# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    tf_val = array_ops.placeholder(dtypes.int32, shape=(4,))[0:2]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([None, None], c_val.as_list())

# begin:end
tf_val = constant_op.constant([10, 20, 30])[1:3]
c_val = tensor_util.constant_value_as_shape(tf_val)
self.assertEqual([20, 30], c_val.as_list())

# begin:end:stride
tf_val = array_ops.strided_slice(
    constant_op.constant([10, 20, 30]), [1], [3], strides=[2])
c_val = tensor_util.constant_value_as_shape(tf_val)
self.assertEqual([20], c_val.as_list())

# [1, 2, 16, 37, None, 48]
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    tf_val_orig = array_ops.concat(
        [[1, 2, 16, 37],
         array_ops.placeholder(dtypes.int32, shape=(1,)), [48]], 0)

    # begin: no end
    tf_val = tf_val_orig[2:]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([16, 37, None, 48], c_val.as_list())

    # begin::negative slice
    tf_val = tf_val_orig[2::-1]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([16, 2, 1], c_val.as_list())

    # :end:negative slice
    tf_val = tf_val_orig[:1:-2]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([48, 37], c_val.as_list())

    # begin:end:negative slice
    tf_val = tf_val_orig[3:1:-1]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([37, 16], c_val.as_list())

    # begin:negative end:slice
    tf_val = tf_val_orig[1:-3:1]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([2, 16], c_val.as_list())

    # negative begin::slice
    tf_val = tf_val_orig[-3::1]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([37, None, 48], c_val.as_list())

    # negative begin::negative slice
    tf_val = tf_val_orig[-3::-1]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([37, 16, 2, 1], c_val.as_list())

    # negative begin:negative end:negative slice
    tf_val = tf_val_orig[-3:-5:-1]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([37, 16], c_val.as_list())

    # Do not support shape inference for additional arguments
    tf_val = constant_op.constant([10, 20, 30])[...]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual([None, None, None], c_val.as_list())

    # Do not support shape inference for tensor slices.
    tf_val = constant_op.constant(
        [10, 20, 30])[array_ops.placeholder(dtypes.int32, shape=()):]
    c_val = tensor_util.constant_value_as_shape(tf_val)
    self.assertEqual(tensor_shape.unknown_shape(), c_val)

    # Do not support shape inference for higher rank
    with self.assertRaises(ValueError):
        tf_val = constant_op.constant([[10], [20], [30]])[:, 0:]
        c_val = tensor_util.constant_value_as_shape(tf_val)
