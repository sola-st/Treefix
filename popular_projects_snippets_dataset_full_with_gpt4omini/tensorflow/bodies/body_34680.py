# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("one_column_3.txt")

with self.cached_session():
    default_value = "UNK"
    key_index = lookup_ops.TextFileIndex.WHOLE_LINE
    value_index = lookup_ops.TextFileIndex.LINE_NUMBER

    with self.assertRaises(ValueError):
        init = lookup_ops.TextFileInitializer(vocabulary_file, dtypes.int64,
                                              key_index, dtypes.string,
                                              value_index)
        self.assertIn("one_column_3.txt_-2_-1", init._shared_name)
        self.getHashTable()(
            init, default_value, experimental_is_anonymous=is_anonymous)
