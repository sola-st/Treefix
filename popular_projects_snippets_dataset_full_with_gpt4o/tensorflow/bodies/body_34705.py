# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self.getVocabularyTable()(
    None, num_oov_buckets=1, experimental_is_anonymous=is_anonymous)
self.assertIsNone(table.resource_handle)
