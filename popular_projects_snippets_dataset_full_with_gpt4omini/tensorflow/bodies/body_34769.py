# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab6.txt")
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Invalid vocab_size"):
    _ = lookup_ops.index_to_string_table_from_file(
        vocabulary_file=vocabulary_file, vocab_size=4)
    self.evaluate(lookup_ops.tables_initializer())
