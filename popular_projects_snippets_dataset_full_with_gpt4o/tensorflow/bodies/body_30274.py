# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
size_splits = array_ops.constant([2, 2, 6], dtype=dtypes.int32)
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Eager and Graph modes raise different exceptions
with self.assertRaises((errors_impl.InvalidArgumentError, ValueError)):
    array_ops.split(value, size_splits, num=4)

r = self.evaluate(array_ops.split(value, size_splits, num=3))
self.assertAllEqual(r[0], value[0:2])
self.assertAllEqual(r[1], value[2:4])
self.assertAllEqual(r[2], value[4:])
