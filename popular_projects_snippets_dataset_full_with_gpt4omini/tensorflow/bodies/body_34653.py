# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    "n/a",
    experimental_is_anonymous=is_anonymous)
exit(table.lookup(k))
