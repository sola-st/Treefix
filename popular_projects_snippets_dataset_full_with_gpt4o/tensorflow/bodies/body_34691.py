# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocab_file = self._createVocabFile("feat_to_id_1.txt")
vocab_size = 3
oov_buckets = 1
table = self.getVocabularyTable()(
    lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size),
    oov_buckets,
    experimental_is_anonymous=is_anonymous)

self.initialize_table(table)

input_string = constant_op.constant(["brain", "salad", "surgery", "UNK"])

out = table.lookup(input_string)
self.assertAllEqual([0, 1, 2, 3], self.evaluate(out))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table.size()))
