# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.assertRaisesRegex(errors_impl.OpError,
                            "keys and values cannot be empty"):
    _ = lookup_ops.index_table_from_tensor(
        vocabulary_list=np.array([], dtype=np.str_), num_oov_buckets=1)
    self.evaluate(lookup_ops.tables_initializer())
