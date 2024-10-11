# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
# This test is purely a test for placeholder inputs which is only applicable
# in graph mode.
with ops.Graph().as_default():
    params = constant_op.constant([[0, 1, 2]])
    indices = constant_op.constant([[0, 0], [0, 0]])
    axis = array_ops.placeholder(dtypes.int32)
    gather_t = array_ops.gather(params, indices, axis=axis)
    # Rank 2 params with rank 2 indices results in a rank 3 shape.
    self.assertEqual([None, None, None], gather_t.shape.as_list())

    # If indices is also unknown the result rank is unknown.
    indices = array_ops.placeholder(dtypes.int32)
    gather_t = array_ops.gather(params, indices, axis=axis)
    self.assertEqual(None, gather_t.shape)
