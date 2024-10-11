# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = -1
keys = ["brain", "salad", "surgery"]
values = [0, 1, 2]
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(
        keys, values, value_dtype=dtypes.int64),
    default_val,
    experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

self.assertAllEqual(3, self.evaluate(table.size()))

input_string = constant_op.constant(["brain", "salad", "tank"])
output = table.lookup(input_string)

result = self.evaluate(output)
self.assertAllEqual([0, 1, -1], result)
