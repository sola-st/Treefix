# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
keys = constant_op.constant([11, 12, 13], dtypes.int64)
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=-1,
    empty_key=0,
    deleted_key=-1,
    initial_num_buckets=4,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))
self.assertAllEqual(4, len(self.evaluate(table.export()[0])))

keys2 = constant_op.constant([12, 99], dtypes.int64)
self.evaluate(table.remove(keys2))
self.assertAllEqual(2, self.evaluate(table.size()))
self.assertAllEqual(4, len(self.evaluate(table.export()[0])))

keys3 = constant_op.constant([13, 14, 15, 16, 17], dtypes.int64)
values3 = constant_op.constant([3, 4, 5, 6, 7], dtypes.int64)

self.evaluate(table.insert(keys3, values3))
self.assertAllEqual(6, self.evaluate(table.size()))
self.assertAllEqual(16, len(self.evaluate(table.export()[0])))

keys4 = constant_op.constant([10, 11, 12, 13, 14, 15, 16, 17, 18],
                             dtypes.int64)
output = table.lookup(keys4)
self.assertAllEqual([-1, 0, -1, 3, 4, 5, 6, 7, -1], self.evaluate(output))
