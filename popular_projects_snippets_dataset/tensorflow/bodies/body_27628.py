# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
keys = dataset_ops.Dataset.range(100)
values = dataset_ops.Dataset.range(100).map(
    lambda x: string_ops.as_string(x * 2))
ds = dataset_ops.Dataset.zip((keys, values))
init = lookup_ops.DatasetInitializer(ds)
table = self.getHashTable()(init, default_value="")
self.initialize_table(table)

output = table.lookup(constant_op.constant([0, 2, 5], dtypes.int64))
result = self.evaluate(output)
self.assertAllEqual(["0", "4", "10"], result)
