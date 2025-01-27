# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# Testing an unkown shape in graph.
with ops.Graph().as_default():
    t = array_ops.space_to_depth(
        array_ops.placeholder(dtypes.float32), block_size=4)
    self.assertEqual(4, t.get_shape().ndims)
