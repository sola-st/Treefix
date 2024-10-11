# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = constant_op.constant(-1, dtypes.int64)
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    default_val,
    experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

row_splits = [0, 2, 3]
input_tensor = ragged_tensor.RaggedTensor.from_row_splits(
    constant_op.constant(["brain", "salad", "tank"]),
    constant_op.constant(row_splits, dtypes.int64))
output = table.lookup(input_tensor)

out = self.evaluate(output)

self.assertAllEqual([0, 1, -1], out.values)
self.assertAllEqual(row_splits, out.row_splits)
