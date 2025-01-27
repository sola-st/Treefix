# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocab_file = self._createVocabFile("feat_to_id_1.txt")
with self.cached_session():
    default_value = "UNK"
    vocab_size = 3
    init = lookup_ops.TextFileStringTableInitializer(
        vocab_file, vocab_size=vocab_size)
    self.assertTrue("feat_to_id_1.txt_3_-1_-2", init._shared_name)
    table = self.getHashTable()(
        init, default_value, experimental_is_anonymous=is_anonymous)

    self.initialize_table(table)

    input_values = constant_op.constant([0, 1, 2, 3], dtypes.int64)

    out = table.lookup(input_values)
    self.assertAllEqual([b"brain", b"salad", b"surgery", b"UNK"],
                        self.evaluate(out))
    self.assertEqual(vocab_size, self.evaluate(table.size()))
