# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocab_file = self._createVocabFile("feat_to_id_5.txt")
with self.cached_session():
    vocab_size = 3
    oov_buckets = 1
    table1 = self.getVocabularyTable()(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size),
        oov_buckets,
        experimental_is_anonymous=is_anonymous)

    self.initialize_table(table1)

    input_string_1 = constant_op.constant(
        ["brain", "salad", "surgery", "UNK"])

    out1 = table1.lookup(input_string_1)

    self.assertAllEqual([0, 1, 2, 3], self.evaluate(out1))
    self.assertEqual(vocab_size + oov_buckets, self.evaluate(table1.size()))

with self.cached_session():
    vocab_size = 3
    oov_buckets = 1

    # Underlying lookup table already initialized in previous session.
    # No need to initialize table2
    table2 = self.getVocabularyTable()(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size),
        oov_buckets,
        experimental_is_anonymous=is_anonymous)

    input_string_2 = constant_op.constant(["fruit", "salad", "UNK"])

    out2 = table2.lookup(input_string_2)

    self.assertAllEqual([3, 1, 3], self.evaluate(out2))
    self.assertEqual(vocab_size + oov_buckets, self.evaluate(table2.size()))
