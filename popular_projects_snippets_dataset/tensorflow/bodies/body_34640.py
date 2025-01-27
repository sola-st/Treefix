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

sp_indices = [[0, 0], [0, 1], [1, 0]]
sp_shape = [2, 2]
input_tensor = sparse_tensor.SparseTensor(
    constant_op.constant(sp_indices, dtypes.int64),
    constant_op.constant(["brain", "salad", "tank"]),
    constant_op.constant(sp_shape, dtypes.int64))
output = table.lookup(input_tensor)

out_indices, out_values, out_shape = self.evaluate(output)

self.assertAllEqual([0, 1, -1], out_values)
self.assertAllEqual(sp_indices, out_indices)
self.assertAllEqual(sp_shape, out_shape)
