# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
x = array_ops.zeros([1, 100])
y = array_ops.reshape(
    x, [tensor_shape.Dimension(100),
        tensor_shape.Dimension(1)])
self.assertEqual([100, 1], y.get_shape().as_list())
y = array_ops.reshape(x, tensor_shape.TensorShape([100, 1]))
self.assertEqual([100, 1], y.get_shape().as_list())
