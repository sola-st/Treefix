# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
init = lookup_ops.KeyValueTensorInitializer(
    ("brain", "salad", "surgery"), (0, 1, 2), dtypes.string, dtypes.int64)
table = self.getHashTable()(
    init, default_value=-1, experimental_is_anonymous=is_anonymous)
self.initialize_table(table)
