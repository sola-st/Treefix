# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
self.assertRaises(
    ValueError, lookup_ops.index_table_from_file, vocabulary_file=None)
