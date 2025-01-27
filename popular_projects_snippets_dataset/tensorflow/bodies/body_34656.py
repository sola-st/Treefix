# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(keys, values),
    -1,
    experimental_is_anonymous=is_anonymous)
exit(table.lookup(x))
