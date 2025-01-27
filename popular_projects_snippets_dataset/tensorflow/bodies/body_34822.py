# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = "n/a"
keys = constant_op.constant([0, 1, 2], dtypes.int64)
values = constant_op.constant(["brain", "salad", "surgery"])
table = lookup_ops.MutableHashTable(
    dtypes.int64,
    dtypes.string,
    default_val,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))

input_string = constant_op.constant([0, 1, 3], dtypes.int64)
output = table.lookup(input_string)

result = self.evaluate(output)
self.assertAllEqual((b"brain", b"salad", b"n/a"), result)
