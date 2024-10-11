# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocab_file = self._createVocabFile("feat_to_id_4.txt")
vocab_size = 3
oov_buckets = 3

init = lookup_ops.TextFileIdTableInitializer(
    vocab_file, vocab_size=vocab_size)
table1 = self.getVocabularyTable()(
    init,
    oov_buckets,
    name="table1",
    experimental_is_anonymous=is_anonymous)

table2 = self.getVocabularyTable()(
    init,
    oov_buckets,
    name="table2",
    experimental_is_anonymous=is_anonymous)

self.evaluate(lookup_ops.tables_initializer())

input_string = constant_op.constant(
    ["fruit", "brain", "salad", "surgery", "UNK"])

out1 = table1.lookup(input_string)
out2 = table2.lookup(input_string)

out1, out2 = self.evaluate([out1, out2])
self.assertAllEqual([5, 0, 1, 2, 5], out1)
self.assertAllEqual([5, 0, 1, 2, 5], out2)
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table1.size()))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table2.size()))
