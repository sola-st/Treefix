# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
keys = constant_op.constant([11, 12, 13], dtypes.int64)
values = constant_op.constant([[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]],
                              dtypes.int64)
default_value = constant_op.constant([-1, -2, -3, -4], dtypes.int64)
table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=default_value,
    empty_key=0,
    deleted_key=-1,
    initial_num_buckets=4,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))
self.assertAllEqual(4, len(self.evaluate(table.export()[0])))

self.evaluate(
    table.insert(
        constant_op.constant([14], dtypes.int64),
        constant_op.constant([[2, 3, 4, 5]], dtypes.int64)))
self.assertAllEqual(4, self.evaluate(table.size()))
self.assertAllEqual(8, len(self.evaluate(table.export()[0])))

remove_string = constant_op.constant([12, 16], dtypes.int64)
self.evaluate(table.remove(remove_string))
self.assertAllEqual(3, self.evaluate(table.size()))
self.assertAllEqual(8, len(self.evaluate(table.export()[0])))

input_string = constant_op.constant([11, 12, 14, 15], dtypes.int64)
output = table.lookup(input_string)
self.assertAllEqual([4, 4],
                    output.shape,
                    msg="Saw shape: %s" % output.shape)

result = self.evaluate(output)
self.assertAllEqual(
    [[0, 1, 2, 3], [-1, -2, -3, -4], [2, 3, 4, 5], [-1, -2, -3, -4]],
    result)
