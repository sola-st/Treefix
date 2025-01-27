# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = -1
keys = constant_op.constant([["brain", "salad"], ["surgery", "tank"]])
values = constant_op.constant([[0, 1], [2, 3]], dtypes.int64)
table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

self.evaluate(table.insert(keys, values))
self.assertAllEqual(4, self.evaluate(table.size()))

input_string = constant_op.constant(["brain", "salad", "tank", "tarkus"])
output = table.lookup(input_string)

result = self.evaluate(output)
self.assertAllEqual([0, 1, 3, -1], result)
