# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
p1 = array_ops.placeholder(dtypes.float32)
c1 = constant_op.constant(10.0, shape=[4, 4, 4, 4])
p2 = array_ops.placeholder(dtypes.float32)
c2 = constant_op.constant(20.0, shape=[4, 4, 4, 4])
dim = array_ops.placeholder(dtypes.int32)
concat = array_ops.concat([p1, c1, p2, c2], dim)
self.assertEqual(4, concat.get_shape().ndims)

# All dimensions unknown.
concat2 = array_ops.concat([p1, p2], dim)
self.assertEqual(None, concat2.get_shape())

# Rank doesn't match.
c3 = constant_op.constant(30.0, shape=[4, 4, 4])
with self.assertRaises(ValueError):
    array_ops.concat([p1, c1, p2, c3], dim)
