# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
# Insert 6 keys into a table with 8 buckets.
# The values are chosen to make sure collisions occur when using GCC STL
keys = constant_op.constant([11, 12, 13, 19, 20, 21], dtypes.int64)
values = constant_op.constant([51, 52, 53, 54, 55, 56], dtypes.int64)
table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=-1,
    empty_key=0,
    deleted_key=-1,
    initial_num_buckets=8,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(6, self.evaluate(table.size()))

input_string = constant_op.constant([10, 11, 12, 13, 14, 19, 20, 21, 22],
                                    dtypes.int64)
output = table.lookup(input_string)
self.assertAllEqual([9], output.get_shape())

result = self.evaluate(output)
self.assertAllEqual([-1, 51, 52, 53, -1, 54, 55, 56, -1], result)
