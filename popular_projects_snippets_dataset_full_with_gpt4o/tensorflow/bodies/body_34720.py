# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
keys = constant_op.constant([11, 12, 13, 14], dtypes.int64)
values = constant_op.constant([1, 2, 3, 4], dtypes.int64)
table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=-1,
    empty_key=100,
    deleted_key=200,
    initial_num_buckets=8,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(4, self.evaluate(table.size()))

keys2 = constant_op.constant([12, 15], dtypes.int64)
self.evaluate(table.remove(keys2))
self.assertAllEqual(3, self.evaluate(table.size()))

exported_keys, exported_values = table.export()

np_keys = self.evaluate(exported_keys)
np_values = self.evaluate(exported_values)

self.assertAllEqual(8, len(np_keys))
self.assertAllEqual(8, len(np_values))

# pair up keys and values, drop extra added dimension
pairs = np.dstack((np_keys.flatten(), np_values.flatten()))[0]
# sort by key
pairs = pairs[pairs[:, 0].argsort()]
self.assertAllEqual([[11, 1], [13, 3], [14, 4], [100, 0], [100, 0],
                     [100, 0], [100, 0], [200, 2]], pairs)
