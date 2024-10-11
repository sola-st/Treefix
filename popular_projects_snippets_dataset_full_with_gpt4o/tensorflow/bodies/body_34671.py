# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with ops.name_scope("table_scope"):
    init1 = lookup_ops.KeyValueTensorInitializer(
        ("brain", "salad", "surgery"), (0, 1, 2), dtypes.string, dtypes.int64)
    table1 = self.getHashTable()(
        init1, default_value=-1, experimental_is_anonymous=is_anonymous)
    if not context.executing_eagerly():
        self.assertEqual("hash_table", table1.name)
        self.assertEqual("table_scope/hash_table",
                         table1.resource_handle.op.name)
    init2 = lookup_ops.KeyValueTensorInitializer(
        ("brain", "salad", "surgery"), (0, 1, 2), dtypes.string, dtypes.int64)
    table2 = self.getHashTable()(
        init2, default_value=-1, experimental_is_anonymous=is_anonymous)
    if not context.executing_eagerly():
        self.assertEqual("hash_table_1", table2.name)
        self.assertEqual("table_scope/hash_table_1",
                         table2.resource_handle.op.name)
