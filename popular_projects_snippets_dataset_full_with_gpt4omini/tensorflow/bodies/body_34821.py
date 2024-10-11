# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = -1.0
keys = constant_op.constant([3, 7, 0], dtypes.int64)
values = constant_op.constant([7.5, -1.2, 9.9], dtypes.float32)
table = lookup_ops.MutableHashTable(
    dtypes.int64,
    dtypes.float32,
    default_val,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))

input_string = constant_op.constant([7, 0, 11], dtypes.int64)
output = table.lookup(input_string)

result = self.evaluate(output)
self.assertAllClose([-1.2, 9.9, default_val], result)
