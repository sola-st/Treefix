# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
t = self.batch_to_space(
    array_ops.placeholder(dtypes.float32),
    array_ops.placeholder(dtypes.int32),
    block_size=4)
self.assertEqual(4, t.get_shape().ndims)
