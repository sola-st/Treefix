# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.assertRaisesRegex(ValueError,
                            "`vocabulary_list` must be specified"):
    lookup_ops.index_table_from_tensor(
        vocabulary_list=None, num_oov_buckets=1)
