# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
# This test is purely a test for placeholder inputs which is only applicable
# in graph mode.
with ops.Graph().as_default():
    params = constant_op.constant([[0, 1, 2]])
    indices = array_ops.placeholder(dtypes.int32)
    gather_t = array_ops.gather(params, indices)
    self.assertEqual(None, gather_t.get_shape())
