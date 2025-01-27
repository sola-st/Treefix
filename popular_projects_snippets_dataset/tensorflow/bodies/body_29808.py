# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
t = array_ops.depth_to_space(
    array_ops.placeholder(dtypes.float32), block_size=4)
self.assertEqual(4, t.get_shape().ndims)
