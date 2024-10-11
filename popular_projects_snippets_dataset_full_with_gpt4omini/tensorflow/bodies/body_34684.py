# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
with self.cached_session():
    default_value = -1
    vocab_size = 3
    vocabulary_file1 = self._createVocabFile("one_column6.txt")
    init1 = lookup_ops.TextFileInitializer(
        vocabulary_file1,
        dtypes.string,
        lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64,
        lookup_ops.TextFileIndex.LINE_NUMBER,
        vocab_size=vocab_size)
    self.assertIn("one_column6.txt_3_-2_-1", init1._shared_name)
    table1 = self.getHashTable()(
        init1, default_value, experimental_is_anonymous=is_anonymous)

    # Initialize from file.
    self.initialize_table(table1)
    self.assertEqual(vocab_size, self.evaluate(table1.size()))

    vocabulary_file2 = self._createVocabFile("one_column7.txt")
    vocab_size = 5
    init2 = lookup_ops.TextFileInitializer(
        vocabulary_file2,
        dtypes.string,
        lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64,
        lookup_ops.TextFileIndex.LINE_NUMBER,
        vocab_size=vocab_size)
    self.assertIn("one_column7.txt_5_-2_-1", init2._shared_name)
    with self.assertRaisesOpError("Invalid vocab_size"):
        table2 = self.getHashTable()(
            init2, default_value, experimental_is_anonymous=is_anonymous)
        self.initialize_table(table2)

    vocab_size = 1
    vocabulary_file3 = self._createVocabFile("one_column3.txt")
    init3 = lookup_ops.TextFileInitializer(
        vocabulary_file3,
        dtypes.string,
        lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64,
        lookup_ops.TextFileIndex.LINE_NUMBER,
        vocab_size=vocab_size)
    self.assertIn("one_column3.txt_1_-2_-1", init3._shared_name)
    table3 = self.getHashTable()(
        init3, default_value, experimental_is_anonymous=is_anonymous)

    # Smaller vocab size reads only vocab_size records.
    self.initialize_table(table3)
    self.assertEqual(vocab_size, self.evaluate(table3.size()))
