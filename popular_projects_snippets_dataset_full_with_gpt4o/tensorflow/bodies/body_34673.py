# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
init = lookup_ops.KeyValueTensorInitializer((42, 1, -1000), (0, 1, 2),
                                            dtypes.int32, dtypes.int64)
with self.assertRaises(errors_impl.OpError):
    table = self.getHashTable()(
        init, default_value=-1, experimental_is_anonymous=is_anonymous)
    self.initialize_table(table)
