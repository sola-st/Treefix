# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = constant_op.constant([-1, -1], dtypes.int64)
keys = constant_op.constant(["brain", "salad", "surgery", "tarkus"])
values = constant_op.constant([[0, 1], [2, 3], [4, 5], [6, 7]],
                              dtypes.int64)
table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(4, self.evaluate(table.size()))

remove_string = constant_op.constant(["tarkus", "tank"])
self.evaluate(table.remove(remove_string))
self.assertAllEqual(3, self.evaluate(table.size()))

input_string = constant_op.constant(["brain", "salad", "tank"])
output = table.lookup(input_string)
self.assertAllEqual([3, 2], output.get_shape())

result = self.evaluate(output)
self.assertAllEqual([[0, 1], [2, 3], [-1, -1]], result)

exported_keys, exported_values = table.export()
# exported data is in the order of the internal map, i.e. undefined
sorted_keys = np.sort(self.evaluate(exported_keys))
sorted_values = np.sort(self.evaluate(exported_values), axis=0)
self.assertAllEqual([b"brain", b"salad", b"surgery"], sorted_keys)
sorted_expected_values = np.sort([[4, 5], [2, 3], [0, 1]], axis=0)
self.assertAllEqual(sorted_expected_values, sorted_values)
