# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab7.txt")
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Invalid vocab_size"):
    table = lookup_ops.index_table_from_file(
        vocabulary_file=vocabulary_file, vocab_size=4)
    self.evaluate(table.initializer)
