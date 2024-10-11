# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = "n/a"
keys = constant_op.constant([0, 1, 2], dtypes.int32)
values = constant_op.constant(["brain", "salad", "surgery"])
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    default_val,
    experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

input_tensor = constant_op.constant([0, 1, -1])
output = table.lookup(input_tensor)

result = self.evaluate(output)
self.assertAllEqual([b"brain", b"salad", b"n/a"], result)
