# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
keys = constant_op.constant([[0, 1], [1, 2], [1, 3]], dtypes.int64)
values = constant_op.constant([10, 11, 12], dtypes.int64)
empty_key = constant_op.constant([0, 3], dtypes.int64)
deleted_key = constant_op.constant([-1, -1], dtypes.int64)
default_value = constant_op.constant(-1, dtypes.int64)
table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=default_value,
    empty_key=empty_key,
    deleted_key=deleted_key,
    initial_num_buckets=8,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))

self.evaluate(
    table.insert(
        constant_op.constant([[0, 0]], dtypes.int64),
        constant_op.constant([13], dtypes.int64)))
self.assertAllEqual(4, self.evaluate(table.size()))
self.assertAllEqual(8, len(self.evaluate(table.export()[0])))

remove_string = constant_op.constant([[1, 2], [7, 8]], dtypes.int64)
self.evaluate(table.remove(remove_string))
self.assertAllEqual(3, self.evaluate(table.size()))
self.assertAllEqual(8, len(self.evaluate(table.export()[0])))

input_string = constant_op.constant([[0, 1], [1, 2], [1, 3], [0, 2]],
                                    dtypes.int64)
output = table.lookup(input_string)
self.assertAllEqual([4], output.get_shape())

result = self.evaluate(output)
self.assertAllEqual([10, -1, 12, -1], result)
