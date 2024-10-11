# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = constant_op.constant([-1, -1], dtypes.int64)
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([[0, 1], [2, 3], [4, 5]], dtypes.int64)
table1 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table1.size()))
self.evaluate(table1.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table1.size()))

input_string = constant_op.constant(["brain", "salad", "tank"])
expected_output = [[0, 1], [2, 3], [-1, -1]]
output1 = table1.lookup(input_string)
self.assertAllEqual(expected_output, self.evaluate(output1))

exported_keys, exported_values = table1.export()
self.assertAllEqual(3, self.evaluate(exported_keys).size)
self.assertAllEqual(6, self.evaluate(exported_values).size)

# Populate a second table from the exported data
table2 = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table2.size()))
self.evaluate(table2.insert(exported_keys, exported_values))
self.assertAllEqual(3, self.evaluate(table2.size()))

# Verify lookup result is still the same
output2 = table2.lookup(input_string)
self.assertAllEqual(expected_output, self.evaluate(output2))
