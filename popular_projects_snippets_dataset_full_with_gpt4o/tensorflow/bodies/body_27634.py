# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
with ops.Graph().as_default():
    keys = dataset_ops.Dataset.range(100)
    values = dataset_ops.Dataset.range(100).map(string_ops.as_string)
    ds = dataset_ops.Dataset.zip((keys, values))
    init = lookup_ops.DatasetInitializer(ds)
    table = self.getHashTable()(init, default_value="")
    output = table.lookup(constant_op.constant([0, 2, 5], dtypes.int64))
    self.evaluate(core_lookup_ops.tables_initializer())
    result = self.evaluate(output)
self.assertAllEqual(["0", "2", "5"], result)
