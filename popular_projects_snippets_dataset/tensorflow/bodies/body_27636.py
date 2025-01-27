# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
ds = dataset_ops.Dataset.range(100).map(
    lambda x: string_ops.as_string(x * 2))
table = lookup_ops.index_table_from_dataset(ds, key_dtype=dtypes.int64)
output = table.lookup(
    constant_op.constant(["0", "2", "4"], dtype=dtypes.string))
self.evaluate(core_lookup_ops.tables_initializer())
result = self.evaluate(output)
self.assertAllEqual([0, 1, 2], result)
