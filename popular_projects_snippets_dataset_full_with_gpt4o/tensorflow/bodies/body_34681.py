# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("one_column_4.txt")
with self.cached_session():
    default_value = -1
    key_index = 1  # second column of the line
    value_index = lookup_ops.TextFileIndex.LINE_NUMBER
    init = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.string, key_index, dtypes.int64, value_index)
    self.assertIn("one_column_4.txt_1_-1", init._shared_name)

    with self.assertRaisesOpError("Invalid number of columns"):
        table = self.getHashTable()(
            init, default_value, experimental_is_anonymous=is_anonymous)
        self.initialize_table(table)
