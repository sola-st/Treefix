# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
keys = dataset_ops.Dataset.from_tensor_slices([2, 3, 4])
values = dataset_ops.Dataset.from_tensor_slices(["two", "three", "four"])
ds = dataset_ops.Dataset.zip((keys, values))
table = lookup_ops.table_from_dataset(
    ds, default_value="n/a", key_dtype=dtypes.int64)
output = table.lookup(constant_op.constant([2, 3, 4], dtypes.int32))
self.evaluate(core_lookup_ops.tables_initializer())
result = self.evaluate(output)
self.assertAllEqual(["two", "three", "four"], result)
