# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# Non-vector dimensions.
with self.assertRaises(ValueError):
    array_ops.fill([[0, 1], [2, 3]], 1.0)

# Non-scalar value.
with self.assertRaises(ValueError):
    array_ops.fill([3, 2], [1.0, 2.0])

# Partial dimension information.
f = array_ops.fill(array_ops.placeholder(dtypes_lib.int32, shape=(4,)), 3.0)
self.assertEqual([None, None, None, None], f.get_shape().as_list())

f = array_ops.fill(
    [array_ops.placeholder(
        dtypes_lib.int32, shape=()), 17], 1.0)
self.assertEqual([None, 17], f.get_shape().as_list())
