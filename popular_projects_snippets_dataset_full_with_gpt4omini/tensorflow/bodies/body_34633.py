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
self.assertEqual(table._is_anonymous, is_anonymous)
self.initialize_table(table)

self.assertAllEqual(3, self.evaluate(table.size()))

input_string = constant_op.constant(["brain", "salad", "tank"])
output = table.lookup(input_string)
self.assertAllEqual([3], output.get_shape())

result = self.evaluate(output)
self.assertAllEqual([0, 1, -1], result)

exported_keys_tensor, exported_values_tensor = table.export()

self.assertItemsEqual([b"brain", b"salad", b"surgery"],
                      self.evaluate(exported_keys_tensor))
self.assertItemsEqual([0, 1, 2], self.evaluate(exported_values_tensor))
