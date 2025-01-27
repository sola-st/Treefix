# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab9.txt")
table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file, num_oov_buckets=1)
self.assertIsNotNone(table.resource_handle)
