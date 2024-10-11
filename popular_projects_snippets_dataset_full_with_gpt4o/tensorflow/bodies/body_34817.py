# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)

table1 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)
table2 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)
table3 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)
self.evaluate(table1.insert(keys, values))
self.evaluate(table2.insert(keys, values))
self.evaluate(table3.insert(keys, values))

self.assertAllEqual(3, self.evaluate(table1.size()))
self.assertAllEqual(3, self.evaluate(table2.size()))
self.assertAllEqual(3, self.evaluate(table3.size()))

input_string = constant_op.constant(["brain", "salad", "tank"])
output1 = table1.lookup(input_string)
output2 = table2.lookup(input_string)
output3 = table3.lookup(input_string)

out1, out2, out3 = self.evaluate([output1, output2, output3])
self.assertAllEqual([0, 1, -1], out1)
self.assertAllEqual([0, 1, -1], out2)
self.assertAllEqual([0, 1, -1], out3)
