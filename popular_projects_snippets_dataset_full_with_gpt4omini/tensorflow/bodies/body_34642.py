# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    default_val,
    experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

# Ref types do not produce a lookup signature mismatch.
input_string_ref = variables.Variable("brain")
self.evaluate(input_string_ref.initializer)
self.assertEqual(0, self.evaluate(table.lookup(input_string_ref)))

input_string = constant_op.constant([1, 2, 3], dtypes.int64)
with self.assertRaises(TypeError):
    table.lookup(input_string)

with self.assertRaises(TypeError):
    self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(keys, values),
        "UNK",
        experimental_is_anonymous=is_anonymous)
