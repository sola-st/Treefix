# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py

# Testing unknown shapes in graph building.
with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32)

    # Unknown input shape, partial new shape.
    y = array_ops.reshape(x, [1, 1, -1, 1])
    self.assertEqual([1, 1, None, 1], y.get_shape().as_list())

    # Unknown input shape, unknown new shape.
    y = array_ops.reshape(x, array_ops.placeholder(dtypes.int32))
    self.assertEqual(None, y.get_shape().ndims)

    # Unknown input shape, known rank for new shape.
    y = array_ops.reshape(x, array_ops.placeholder(dtypes.int32, shape=(3,)))
    self.assertEqual([None, None, None], y.get_shape().as_list())

    # Unknown input shape, partial new shape using `tf.stack()`.
    y = array_ops.reshape(x, [array_ops.placeholder(dtypes.int32), 37])
    self.assertEqual([None, 37], y.get_shape().as_list())

    # Unknown input shape, partial new shape using `tf.concat()`.
    y = array_ops.reshape(
        x,
        array_ops.concat(
            [array_ops.placeholder(
                dtypes.int32, shape=(2,)), [37, 42]], 0))
    self.assertEqual([None, None, 37, 42], y.get_shape().as_list())

    # Unknown input shape, partial new shape using `tf.shape()`.
    y = array_ops.reshape(
        x,
        array_ops.shape(
            array_ops.placeholder(
                dtypes.float32, shape=[None, 37, None])))
    self.assertEqual([None, 37, None], y.get_shape().as_list())
