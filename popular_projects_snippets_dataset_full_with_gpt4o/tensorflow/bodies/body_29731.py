# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    params = constant_op.constant([[0, 1, 2]])
    indices = array_ops.placeholder(dtypes.int32, shape=[None, None])
    gather_t = array_ops.batch_gather(params, indices)
    self.assertEqual([1, None], gather_t.get_shape().as_list())
