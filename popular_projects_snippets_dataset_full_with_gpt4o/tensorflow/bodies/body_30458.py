# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# Shape function requires placeholders and a graph
with ops.Graph().as_default():
    # Unknown paddings shape.
    inp = constant_op.constant(0.0, shape=[4, 4, 4, 4])
    padded = array_ops.pad(inp, array_ops.placeholder(dtypes.int32))
    self.assertEqual([None, None, None, None], padded.get_shape().as_list())

    # Unknown input shape.
    inp = array_ops.placeholder(dtypes.float32)
    padded = array_ops.pad(inp, [[2, 2], [2, 2]])
    self.assertEqual([None, None], padded.get_shape().as_list())

    # Unknown input and paddings shape.
    inp = array_ops.placeholder(dtypes.float32)
    padded = array_ops.pad(inp, array_ops.placeholder(dtypes.int32))
    self.assertAllEqual(None, padded.get_shape().ndims)
